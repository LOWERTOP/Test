import re

def parse_module_file(module_file_path):
    """解析 Talkatone.sgmodule 文件中的所有规则"""
    with open(module_file_path, 'r') as file:
        content = file.read()

    # 使用正则表达式提取所有类型的规则（包括 IP-CIDR、DOMAIN-SUFFIX、DOMAIN-KEYWORD 等）
    reject_rules = re.findall(r'([A-Z\-]+,[^,]+,REJECT.*)', content)
    reject_drop_rules = re.findall(r'([A-Z\-]+,[^,]+,REJECT-DROP.*)', content)
    direct_rules = re.findall(r'([A-Z\-]+,[^,]+,DIRECT.*)', content)
    proxy_rules = re.findall(r'([A-Z\-]+,[^,]+,PROXY.*)', content)
    ip_cidr_reject_rules = re.findall(r'(IP-CIDR,[^,]+,REJECT.*)', content)
    ip_cidr_direct_rules = re.findall(r'(IP-CIDR,[^,]+,DIRECT.*)', content)
    ip_cidr_proxy_rules = re.findall(r'(IP-CIDR,[^,]+,PROXY.*)', content)

    # 合并所有相关的规则
    reject_rules += reject_drop_rules + ip_cidr_reject_rules
    direct_rules += ip_cidr_direct_rules
    proxy_rules += ip_cidr_proxy_rules

    # 只保留规则部分（去掉 REJECT、DIRECT、PROXY 等策略）
    reject_rules = [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in reject_rules]
    direct_rules = [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in direct_rules]
    proxy_rules = [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in proxy_rules]

    # 去重并排序
    reject_rules = sorted(set(reject_rules))
    direct_rules = sorted(set(direct_rules))
    proxy_rules = sorted(set(proxy_rules))

    return reject_rules, direct_rules, proxy_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules

def add_no_resolve_to_ip_rules(ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules):
    """对 IP-CIDR 类型的规则添加 no-resolve 参数，仅当该规则不包含 no-resolve 时添加"""
    def add_no_resolve(rules):
        updated_rules = []
        for rule in rules:
            # 仅当规则不包含 no-resolve 时才添加
            if 'no-resolve' not in rule:
                rule += ',no-resolve'
            updated_rules.append(rule)
        return updated_rules

    ip_cidr_reject_rules = add_no_resolve(ip_cidr_reject_rules)
    ip_cidr_direct_rules = add_no_resolve(ip_cidr_direct_rules)
    ip_cidr_proxy_rules = add_no_resolve(ip_cidr_proxy_rules)

    return ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules

def remove_duplicates(rules):
    """去重规则，确保每条规则唯一"""
    seen = set()
    clean_rules = []
    for rule in rules:
        if rule not in seen:
            seen.add(rule)
            clean_rules.append(rule)
    return clean_rules

def remove_proxy_from_ip_cidr_rules(ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules):
    """从 IP-CIDR 规则中删除代理策略（如 DIRECT, PROXY）"""
    def remove_proxy(rules):
        updated_rules = []
        for rule in rules:
            # 删除规则中的代理策略，只保留 IP 地址和 no-resolve 参数
            parts = rule.split(',')
            if len(parts) > 2:  # 如果规则包含代理策略
                updated_rule = ','.join(parts[:2]) + ',no-resolve'  # 只保留前两部分并添加 no-resolve
            else:
                updated_rule = rule  # 没有代理策略的规则
            updated_rules.append(updated_rule)
        return updated_rules

    ip_cidr_reject_rules = remove_proxy(ip_cidr_reject_rules)
    ip_cidr_direct_rules = remove_proxy(ip_cidr_direct_rules)
    ip_cidr_proxy_rules = remove_proxy(ip_cidr_proxy_rules)

    return ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules

def update_list_file(list_file_path, rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type):
    """
    更新 .list 文件中的规则，保留原注释，替换规则部分
    :param list_file_path: .list 文件路径
    :param rules: 规则列表
    :param ip_cidr_reject_rules: IP-CIDR REJECT 规则
    :param ip_cidr_direct_rules: IP-CIDR DIRECT 规则
    :param ip_cidr_proxy_rules: IP-CIDR PROXY 规则
    :param rule_type: 当前子文件规则类型（REJECT、DIRECT、PROXY）
    """
    with open(list_file_path, 'r') as file:
        content = file.readlines()

    updated_content = []
    rules_updated = False

    # 保留注释行
    for line in content:
        if line.startswith('#'):
            updated_content.append(line)

    updated_content.append("\n")  # 保证注释与规则之间有空行
    
    # 根据 rule_type 选择性添加规则
    if rule_type == "REJECT":
        updated_content.extend([rule + '\n' for rule in rules])  # 只添加 REJECT 规则
        if ip_cidr_reject_rules:
            updated_content.append("\n")  # 空一行
            updated_content.extend([rule + '\n' for rule in ip_cidr_reject_rules])  # 添加 IP-CIDR REJECT 规则
    elif rule_type == "DIRECT":
        updated_content.extend([rule + '\n' for rule in rules])  # 只添加 DIRECT 规则
        if ip_cidr_direct_rules:
            updated_content.append("\n")  # 空一行
            updated_content.extend([rule + '\n' for rule in ip_cidr_direct_rules])  # 添加 IP-CIDR DIRECT 规则
    elif rule_type == "PROXY":
        updated_content.extend([rule + '\n' for rule in rules])  # 只添加 PROXY 规则
        if ip_cidr_proxy_rules:
            updated_content.append("\n")  # 空一行
            updated_content.extend([rule + '\n' for rule in ip_cidr_proxy_rules])  # 添加 IP-CIDR PROXY 规则

    # 写回更新后的内容
    with open(list_file_path, 'w') as file:
        file.writelines(updated_content)

    print(f"Updated {list_file_path}")  # 日志输出

def update_rule_files():
    """更新所有相关的 .list 文件"""
    module_path = './Talkatone.sgmodule'
    reject_rules, direct_rules, proxy_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules = parse_module_file(module_path)

    # 对 IP 类的规则添加 no-resolve 参数
    ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules = add_no_resolve_to_ip_rules(ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules)

    # 去除代理策略（DIRECT、PROXY）并保留 no-resolve 参数
    ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules = remove_proxy_from_ip_cidr_rules(ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules)

    # 最后去重和检查 no-resolve 参数
    reject_rules = remove_duplicates(reject_rules)
    direct_rules = remove_duplicates(direct_rules)
    proxy_rules = remove_duplicates(proxy_rules)

    ip_cidr_reject_rules = remove_duplicates(ip_cidr_reject_rules)
    ip_cidr_direct_rules = remove_duplicates(ip_cidr_direct_rules)
    ip_cidr_proxy_rules = remove_duplicates(ip_cidr_proxy_rules)

    # 更新各个 .list 文件
    update_list_file('./TalkatoneAntiAds.list', reject_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type="REJECT")
    update_list_file('./TalkatoneDirect.list', direct_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type="DIRECT")
    update_list_file('./TalkatoneProxy.list', proxy_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type="PROXY")
    update_list_file('./TalkatoneProxyOnly.list', proxy_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type="PROXY")

# 执行更新操作
update_rule_files()

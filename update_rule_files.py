import re

def parse_module_file(module_file_path):
    """解析母文件 Talkatone.sgmodule 中的所有规则"""
    with open(module_file_path, 'r') as file:
        content = file.read()

    # 使用正则表达式提取规则（包括 IP-CIDR、DOMAIN-SUFFIX、DOMAIN-KEYWORD 等）
    reject_rules = re.findall(r'([A-Z\-]+,[^,]+,REJECT.*)', content)
    direct_rules = re.findall(r'([A-Z\-]+,[^,]+,DIRECT.*)', content)
    proxy_rules = re.findall(r'([A-Z\-]+,[^,]+,PROXY.*)', content)
    ip_cidr_reject_rules = re.findall(r'(IP-CIDR,[^,]+,REJECT.*)', content)
    ip_cidr_direct_rules = re.findall(r'(IP-CIDR,[^,]+,DIRECT.*)', content)
    ip_cidr_proxy_rules = re.findall(r'(IP-CIDR,[^,]+,PROXY.*)', content)

    # 合并并去重规则
    reject_rules += ip_cidr_reject_rules
    direct_rules += ip_cidr_direct_rules
    proxy_rules += ip_cidr_proxy_rules

    # 只保留规则部分（去掉 REJECT、DIRECT、PROXY 等策略）
    reject_rules = [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in reject_rules]
    direct_rules = [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in direct_rules]
    proxy_rules = [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in proxy_rules]

    # 排序并去重
    reject_rules = sorted(set(reject_rules))
    direct_rules = sorted(set(direct_rules))
    proxy_rules = sorted(set(proxy_rules))

    return reject_rules, direct_rules, proxy_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules


def add_no_resolve(rules):
    """检查并为 IP-CIDR 规则添加 no-resolve 参数"""
    updated_rules = []
    for rule in rules:
        if 'no-resolve' not in rule:
            rule += ',no-resolve'
        updated_rules.append(rule)
    return updated_rules


def remove_proxy(rules):
    """去除代理策略（PROXY、DIRECT、REJECT）"""
    return [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in rules]


def update_list_file(list_file_path, rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type):
    """更新 .list 文件中的规则，保留原注释，替换规则部分"""
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
        updated_content.extend([rule + '\n' for rule in rules])
        if ip_cidr_reject_rules:
            updated_content.append("\n")
            updated_content.extend([rule + '\n' for rule in ip_cidr_reject_rules])
    elif rule_type == "DIRECT":
        updated_content.extend([rule + '\n' for rule in rules])
        if ip_cidr_direct_rules:
            updated_content.append("\n")
            updated_content.extend([rule + '\n' for rule in ip_cidr_direct_rules])
    elif rule_type == "PROXY":
        updated_content.extend([rule + '\n' for rule in rules])
        if ip_cidr_proxy_rules:
            updated_content.append("\n")
            updated_content.extend([rule + '\n' for rule in ip_cidr_proxy_rules])

    # 添加 IP 类型规则到文件末尾（仅添加到对应类型的文件）
    if rule_type == "REJECT" and ip_cidr_reject_rules:
        updated_content.append("\n# IP-CIDR REJECT rules\n")
        updated_content.extend([rule + '\n' for rule in ip_cidr_reject_rules])
    if rule_type == "DIRECT" and ip_cidr_direct_rules:
        updated_content.append("\n# IP-CIDR DIRECT rules\n")
        updated_content.extend([rule + '\n' for rule in ip_cidr_direct_rules])
    if rule_type == "PROXY" and ip_cidr_proxy_rules:
        updated_content.append("\n# IP-CIDR PROXY rules\n")
        updated_content.extend([rule + '\n' for rule in ip_cidr_proxy_rules])

    # 写回更新后的内容
    with open(list_file_path, 'w') as file:
        file.writelines(updated_content)

    print(f"Updated {list_file_path}")


def update_rule_files():
    """更新所有相关的 .list 文件"""
    module_path = './Talkatone.sgmodule'
    reject_rules, direct_rules, proxy_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules = parse_module_file(module_path)

    # 对 IP 类型的规则添加 no-resolve 参数
    ip_cidr_reject_rules = add_no_resolve(ip_cidr_reject_rules)
    ip_cidr_direct_rules = add_no_resolve(ip_cidr_direct_rules)
    ip_cidr_proxy_rules = add_no_resolve(ip_cidr_proxy_rules)

    # 去除代理策略（DIRECT、PROXY）并保留 no-resolve 参数
    reject_rules = remove_proxy(reject_rules)
    direct_rules = remove_proxy(direct_rules)
    proxy_rules = remove_proxy(proxy_rules)

    # 去重并排序
    reject_rules = sorted(set(reject_rules))
    direct_rules = sorted(set(direct_rules))
    proxy_rules = sorted(set(proxy_rules))

    ip_cidr_reject_rules = sorted(set(ip_cidr_reject_rules))
    ip_cidr_direct_rules = sorted(set(ip_cidr_direct_rules))
    ip_cidr_proxy_rules = sorted(set(ip_cidr_proxy_rules))

    # 更新各个 .list 文件
    update_list_file('./TalkatoneAntiAds.list', reject_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type="REJECT")
    update_list_file('./TalkatoneDirect.list', direct_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type="DIRECT")
    update_list_file('./TalkatoneProxy.list', reject_rules + direct_rules + proxy_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type="PROXY")
    update_list_file('./TalkatoneProxyOnly.list', proxy_rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type="PROXY")


# 执行更新操作
update_rule_files()

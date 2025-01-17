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
    """对 IP-CIDR 类型的规则添加 no-resolve 参数"""
    ip_cidr_reject_rules = [rule + ',no-resolve' for rule in ip_cidr_reject_rules]
    ip_cidr_direct_rules = [rule + ',no-resolve' for rule in ip_cidr_direct_rules]
    ip_cidr_proxy_rules = [rule + ',no-resolve' for rule in ip_cidr_proxy_rules]

    return ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules

def update_list_file(list_file_path, reject_rules=None, direct_rules=None, proxy_rules=None, ip_cidr_reject_rules=None, ip_cidr_direct_rules=None, ip_cidr_proxy_rules=None):
    """
    更新 .list 文件中的规则，保留原注释，替换规则部分
    :param list_file_path: .list 文件路径
    :param reject_rules: REJECT 规则列表
    :param direct_rules: DIRECT 规则列表
    :param proxy_rules: PROXY 规则列表
    :param ip_cidr_reject_rules: IP-CIDR REJECT 规则
    :param ip_cidr_direct_rules: IP-CIDR DIRECT 规则
    :param ip_cidr_proxy_rules: IP-CIDR PROXY 规则
    """
    with open(list_file_path, 'r') as file:
        content = file.readlines()

    updated_content = []
    reject_updated = False
    direct_updated = False
    proxy_updated = False

    # 遍历原文件内容
    for line in content:
        # 保留注释行
        if line.startswith('#'):
            updated_content.append(line)
        elif ',' in line:  # 检测到规则行
            updated_content.append(line)  # 其他行原样加入

    # 如果某些类型的规则没有被更新，确保插入它们
    if reject_rules and not reject_updated:
        updated_content.extend([rule + '\n' for rule in reject_rules])  # 添加 REJECT 规则
        reject_updated = True
    if direct_rules and not direct_updated:
        updated_content.extend([rule + '\n' for rule in direct_rules])  # 添加 DIRECT 规则
        direct_updated = True
    if proxy_rules and not proxy_updated:
        updated_content.extend([rule + '\n' for rule in proxy_rules])  # 添加 PROXY 规则
        proxy_updated = True

    # 排序规则：根据规则类型和首字母进行排序
    valid_rules = [rule for rule in updated_content if ',' in rule and len(rule.split(',')) > 1]
    sorted_rules = sorted(valid_rules, key=lambda x: (x.split(',')[0], x.split(',')[1].lower()))

    # 将排序后的规则更新到文件内容
    updated_content = [line for line in updated_content if ',' not in line]  # 保留非规则行
    updated_content.extend(sorted_rules)  # 添加排序后的规则

    # 在最后添加 IP-CIDR 规则，并加上 no-resolve
    if ip_cidr_reject_rules:
        updated_content.extend([rule + '\n' for rule in ip_cidr_reject_rules])  # 添加 IP-CIDR REJECT 规则
    if ip_cidr_direct_rules:
        updated_content.extend([rule + '\n' for rule in ip_cidr_direct_rules])  # 添加 IP-CIDR DIRECT 规则
    if ip_cidr_proxy_rules:
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

    # 更新各个 .list 文件
    update_list_file('./TalkatoneAntiAds.list', reject_rules=reject_rules)
    update_list_file('./TalkatoneDirect.list', direct_rules=direct_rules)
    update_list_file('./TalkatoneProxyOnly.list', proxy_rules=proxy_rules)
    update_list_file('./TalkatoneProxy.list', direct_rules=direct_rules, proxy_rules=proxy_rules)

if __name__ == "__main__":
    update_rule_files()

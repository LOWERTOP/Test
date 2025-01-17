import os

def update_list_file(list_file_path, rules, ip_cidr_reject_rules, ip_cidr_direct_rules, ip_cidr_proxy_rules, rule_type):
    print(f"Updating {list_file_path}")  # 调试信息，检查文件路径

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

    # 输出更新后的内容长度，检查是否写入了内容
    print(f"Updated {len(updated_content)} lines in {list_file_path}")

    # 写回更新后的内容
    with open(list_file_path, 'w') as file:
        file.writelines(updated_content)
    
    print(f"Updated {list_file_path} successfully!")  # 完成更新的调试信息

def update_rule_files():
    # 设置母文件路径和子文件路径
    module_file_path = "Talkatone.sgmodule"
    list_file_paths = {
        "TalkatoneAntiAds.list": "REJECT",
        "TalkatoneDirect.list": "DIRECT",
        "TalkatoneProxy.list": "PROXY",
        "TalkatoneProxyOnly.list": "PROXY"
    }

    # 读取母文件内容
    with open(module_file_path, 'r') as module_file:
        module_content = module_file.readlines()

    # 提取不同类型的规则
    reject_rules = [line.strip() for line in module_content if "REJECT" in line]
    direct_rules = [line.strip() for line in module_content if "DIRECT" in line]
    proxy_rules = [line.strip() for line in module_content if "PROXY" in line]

    # 提取 IP-CIDR 规则
    ip_cidr_reject_rules = [line for line in reject_rules if "IP-CIDR" in line]
    ip_cidr_direct_rules = [line for line in direct_rules if "IP-CIDR" in line]
    ip_cidr_proxy_rules = [line for line in proxy_rules if "IP-CIDR" in line]

    # 检查并添加 no-resolve 到 IP-CIDR 规则
    def add_no_resolve_to_ip_rules(rules):
        updated_rules = []
        for rule in rules:
            if "no-resolve" not in rule:
                updated_rules.append(rule + ",no-resolve")
            else:
                updated_rules.append(rule)
        return updated_rules

    ip_cidr_reject_rules = add_no_resolve_to_ip_rules(ip_cidr_reject_rules)
    ip_cidr_direct_rules = add_no_resolve_to_ip_rules(ip_cidr_direct_rules)
    ip_cidr_proxy_rules = add_no_resolve_to_ip_rules(ip_cidr_proxy_rules)

    # 更新每个子文件
    for list_file_name, rule_type in list_file_paths.items():
        list_file_path = list_file_name
        if rule_type == "REJECT":
            update_list_file(list_file_path, reject_rules, ip_cidr_reject_rules, [], [], rule_type)
        elif rule_type == "DIRECT":
            update_list_file(list_file_path, direct_rules, [], ip_cidr_direct_rules, [], rule_type)
        elif rule_type == "PROXY":
            update_list_file(list_file_path, proxy_rules, [], [], ip_cidr_proxy_rules, rule_type)

if __name__ == "__main__":
    update_rule_files()

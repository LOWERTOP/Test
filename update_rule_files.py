import os

def update_list_file(list_file_path, rule_type, new_rules):
    """
    更新子文件函数，确保删除原有规则并写入新的规则。
    :param list_file_path: 子文件路径
    :param rule_type: 当前规则类型（REJECT、DIRECT、PROXY）
    :param new_rules: 新的规则列表
    """
    print(f"Updating {list_file_path} with {rule_type} rules")

    with open(list_file_path, 'r') as file:
        content = file.readlines()

    updated_content = []
    rules_updated = False

    # 保留注释行
    for line in content:
        if line.startswith('#'):
            updated_content.append(line)
    
    updated_content.append("\n")  # 保证注释与规则之间有空行

    # 添加新规则（去除重复规则和无代理策略的规则）
    updated_content.extend([rule + '\n' for rule in new_rules])
    
    # 输出更新后的内容长度，检查是否写入了内容
    print(f"Updated {len(updated_content)} lines in {list_file_path}")

    # 将更新后的内容写回文件
    with open(list_file_path, 'w') as file:
        file.writelines(updated_content)

    print(f"Updated {list_file_path} successfully!")  # 完成更新的调试信息

def extract_rules_by_type(module_content, rule_type):
    """
    从母文件内容中提取指定类型的规则。
    :param module_content: 母文件内容
    :param rule_type: 规则类型（REJECT、DIRECT、PROXY）
    :return: 提取出的规则列表
    """
    return [line.strip() for line in module_content if rule_type in line]

def process_ip_cidr_rules(ip_cidr_rules):
    """
    处理 IP-CIDR 规则，去重并添加 no-resolve。
    :param ip_cidr_rules: 原始 IP-CIDR 规则列表
    :return: 处理后的 IP-CIDR 规则列表
    """
    seen_rules = set()
    processed_rules = []

    for rule in ip_cidr_rules:
        if rule not in seen_rules:
            if "no-resolve" not in rule:
                processed_rules.append(rule + ",no-resolve")
            else:
                processed_rules.append(rule)
            seen_rules.add(rule)

    return processed_rules

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
    reject_rules = extract_rules_by_type(module_content, "REJECT")
    direct_rules = extract_rules_by_type(module_content, "DIRECT")
    proxy_rules = extract_rules_by_type(module_content, "PROXY")

    # 提取 IP-CIDR 规则并处理去重和添加 no-resolve
    ip_cidr_reject_rules = [rule for rule in reject_rules if "IP-CIDR" in rule]
    ip_cidr_direct_rules = [rule for rule in direct_rules if "IP-CIDR" in rule]
    ip_cidr_proxy_rules = [rule for rule in proxy_rules if "IP-CIDR" in rule]

    # 去重并添加 no-resolve
    ip_cidr_reject_rules = process_ip_cidr_rules(ip_cidr_reject_rules)
    ip_cidr_direct_rules = process_ip_cidr_rules(ip_cidr_direct_rules)
    ip_cidr_proxy_rules = process_ip_cidr_rules(ip_cidr_proxy_rules)

    # 更新每个子文件
    for list_file_name, rule_type in list_file_paths.items():
        # 根据规则类型生成更新后的规则
        if rule_type == "REJECT":
            new_rules = reject_rules + ip_cidr_reject_rules
        elif rule_type == "DIRECT":
            new_rules = direct_rules + ip_cidr_direct_rules
        elif rule_type == "PROXY":
            new_rules = proxy_rules + ip_cidr_proxy_rules

        # 更新子文件
        update_list_file(list_file_name, rule_type, new_rules)

if __name__ == "__main__":
    update_rule_files()

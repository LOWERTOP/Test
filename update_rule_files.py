import re

def parse_module_file(module_file_path):
    """解析 Talkatone.sgmodule 文件中的规则"""
    with open(module_file_path, 'r') as file:
        content = file.read()

    # 使用正则表达式提取不同类型的规则
    reject_rules = re.findall(r'DOMAIN-[A-Z]+,[^,]+,REJECT.*', content)
    reject_drop_rules = re.findall(r'DOMAIN-SUFFIX,[^,]+,REJECT-DROP.*', content)
    direct_rules = re.findall(r'DOMAIN-SUFFIX,[^,]+,DIRECT.*', content)
    proxy_rules = re.findall(r'DOMAIN-SUFFIX,[^,]+,PROXY.*', content)

    # 只保留规则部分（去掉 REJECT、DIRECT、PROXY 等策略）
    reject_rules = [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in reject_rules + reject_drop_rules]
    direct_rules = [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in direct_rules]
    proxy_rules = [rule.split(',')[0] + ',' + rule.split(',')[1] for rule in proxy_rules]

    return reject_rules, direct_rules, proxy_rules

def update_list_file(list_file_path, reject_rules, direct_rules, proxy_rules):
    """
    更新 .list 文件中的规则，保留原注释，替换规则部分
    :param list_file_path: .list 文件路径
    :param reject_rules: REJECT 规则列表
    :param direct_rules: DIRECT 规则列表
    :param proxy_rules: PROXY 规则列表
    """
    with open(list_file_path, 'r') as file:
        content = file.readlines()

    updated_content = []
    inside_rules = False
    rule_type = None  # 用于标记当前是更新 REJECT、DIRECT 还是 PROXY 规则

    for line in content:
        # 保留注释行不变
        if line.startswith('#'):
            updated_content.append(line)
        elif line.startswith("DOMAIN-") or line.startswith("DOMAIN-SUFFIX"):
            # 跳过规则行，准备更新规则
            if "REJECT" in line:
                rule_type = "REJECT"
            elif "DIRECT" in line:
                rule_type = "DIRECT"
            elif "PROXY" in line:
                rule_type = "PROXY"

        # 根据 rule_type 更新规则
        if rule_type == "REJECT":
            updated_content.extend(reject_rules)
            rule_type = None  # 更新完成后重置
        elif rule_type == "DIRECT":
            updated_content.extend(direct_rules)
            rule_type = None
        elif rule_type == "PROXY":
            updated_content.extend(proxy_rules)
            rule_type = None

    # 写回更新后的内容
    with open(list_file_path, 'w') as file:
        file.writelines(updated_content)

    print(f"Updated {list_file_path}")  # 日志输出

def update_rule_files():
    """更新所有相关的 .list 文件"""
    module_path = './Talkatone.sgmodule'
    reject_rules, direct_rules, proxy_rules = parse_module_file(module_path)

    # 更新各个 .list 文件
    update_list_file('./TalkatoneAntiAds.list', reject_rules, direct_rules, proxy_rules)
    update_list_file('./TalkatoneDirect.list', reject_rules, direct_rules, proxy_rules)
    update_list_file('./TalkatoneProxyOnly.list', reject_rules, direct_rules, proxy_rules)
    update_list_file('./TalkatoneProxy.list', reject_rules, direct_rules, proxy_rules)

if __name__ == "__main__":
    update_rule_files()

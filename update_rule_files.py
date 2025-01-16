import re

def parse_module_file(module_file_path):
    # 读取模块文件并提取规则
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

def update_list_file(list_file_path, rules, rule_type='ALL'):
    """
    更新 .list 文件中的规则部分，保留原注释，更新规则内容
    :param list_file_path: .list 文件路径
    :param rules: 新的规则内容
    :param rule_type: 指定要更新的规则类型 ('ALL' 表示所有规则, 'DIRECT/PROXY' 表示仅更新相应类型的规则)
    """
    with open(list_file_path, 'r') as file:
        content = file.readlines()

    updated_content = []
    inside_rules = False

    for line in content:
        # 如果当前行是规则部分，更新规则
        if line.startswith("# Rules") or not inside_rules:
            updated_content.append(line)
            if line.startswith("# Rules"):
                inside_rules = True
        elif inside_rules and not line.startswith("#"):
            # 根据规则类型过滤要更新的内容
            if rule_type == 'ALL':
                updated_content.append(rules)  # 更新所有规则
            elif rule_type == 'DIRECT/PROXY':
                # 对于 TalkatoneProxy.list 仅更新 DIRECT 和 PROXY 规则
                updated_content.append("\n".join(rules))
            inside_rules = False
        else:
            updated_content.append(line)

    # 写回更新后的内容
    with open(list_file_path, 'w') as file:
        file.writelines(updated_content)

    print(f"Updated {list_file_path}")  # 日志输出

def update_rule_files():
    module_path = './Talkatone.sgmodule'
    reject_rules, direct_rules, proxy_rules = parse_module_file(module_path)

    # 构造规则内容
    reject_rules_str = "\n".join(reject_rules)
    direct_rules_str = "\n".join(direct_rules)
    proxy_rules_str = "\n".join(proxy_rules)

    # 更新 .list 文件
    update_list_file('./TalkatoneAntiAds.list', reject_rules_str, rule_type='ALL')
    update_list_file('./TalkatoneDirect.list', direct_rules_str, rule_type='ALL')
    update_list_file('./TalkatoneProxyOnly.list', proxy_rules_str, rule_type='ALL')
    
    # 只更新 DIRECT 和 PROXY 规则到 TalkatoneProxy.list，去掉 REJECT
    update_list_file('./TalkatoneProxy.list', direct_rules + proxy_rules, rule_type='DIRECT/PROXY')

if __name__ == "__main__":
    update_rule_files()

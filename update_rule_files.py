import re

def update_list_file(source_file, target_file, rule_type):
    # 读取母文件
    with open(source_file, 'r') as src:
        source_content = src.read()
    
    # 提取母文件中的规则
    pattern = rf'#\s*{rule_type}.*?\n((?:.*\n)+?)#\s*(?:END|BEGIN)\s*{rule_type}'
    rules = re.findall(pattern, source_content, re.DOTALL)

    # 读取子文件
    with open(target_file, 'r') as tgt:
        target_content = tgt.read()

    # 保留子文件内的注释并删除旧规则
    comment_section = re.findall(r'#.*', target_content)
    new_content = "\n".join(comment_section)  # 保留注释部分

    # 合并新规则
    new_rules = rules[0].strip().splitlines() if rules else []
    new_rules = [rule for rule in new_rules if 'PROXY' not in rule and 'DIRECT' not in rule and 'REJECT' not in rule]
    
    # 排序规则
    ip_rules = [rule for rule in new_rules if re.match(r'^\d{1,3}(\.\d{1,3}){3}', rule)]
    other_rules = [rule for rule in new_rules if rule not in ip_rules]
    
    # IP类规则添加no-resolve
    ip_rules = [rule + ' ,no-resolve' for rule in ip_rules]
    
    # 合并并排序
    sorted_rules = sorted(other_rules) + sorted(ip_rules)
    
    # 更新子文件内容
    new_content += "\n\n" + "\n".join(sorted_rules) + "\n"
    
    # 写入更新后的内容到子文件
    with open(target_file, 'w') as tgt:
        tgt.write(new_content)

if __name__ == '__main__':
    update_list_file('Talkatone.sgmodule', 'TalkatoneAntiAds.list', 'REJECT')
    update_list_file('Talkatone.sgmodule', 'TalkatoneDirect.list', 'Direct')
    update_list_file('Talkatone.sgmodule', 'TalkatoneProxy.list', 'Proxy')
    update_list_file('Talkatone.sgmodule', 'TalkatoneProxyOnly.list', 'Proxy')

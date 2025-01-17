import re

def update_list_file(source_file, target_file, rule_type):
    print(f"Updating {target_file} based on {source_file} with {rule_type} rules...")
    
    # 读取母文件
    with open(source_file, 'r') as src:
        source_content = src.read()
    
    # 解析母文件规则部分
    start_marker = f'# {rule_type}'
    end_marker = f'# END {rule_type}'
    
    start_idx = source_content.find(start_marker)
    end_idx = source_content.find(end_marker, start_idx)
    
    if start_idx == -1 or end_idx == -1:
        print(f"未找到 {rule_type} 规则部分")
        return
    
    # 获取规则内容
    rules_content = source_content[start_idx + len(start_marker): end_idx].strip()
    rules = [rule.strip() for rule in rules_content.split('\n') if rule.strip()]

    print(f"Extracted {len(rules)} rules of type {rule_type}")

    # 读取子文件
    with open(target_file, 'r') as tgt:
        target_content = tgt.read()

    # 提取子文件中的注释部分
    comment_section = []
    lines = target_content.split('\n')
    for line in lines:
        if line.strip().startswith('#'):
            comment_section.append(line)

    # 保留注释并删除旧规则
    new_content = '\n'.join(comment_section) + '\n\n'

    # 排除PROXY/DIRECT/REJECT标签的规则
    new_rules = [rule for rule in rules if 'PROXY' not in rule and 'DIRECT' not in rule and 'REJECT' not in rule]

    # IP类规则和其他规则分开处理
    ip_rules = []
    other_rules = []
    
    for rule in new_rules:
        if re.search(r'\d+\.\d+\.\d+\.\d+', rule):  # 检查是否为IP规则
            ip_rules.append(rule)
        else:
            other_rules.append(rule)

    # 添加no-resolve标记到IP规则
    ip_rules = [rule + ' ,no-resolve' for rule in ip_rules]

    # 合并规则并排序
    sorted_rules = sorted(other_rules) + sorted(ip_rules)

    print(f"Writing {len(sorted_rules)} rules to {target_file}...")

    # 更新子文件内容
    new_content += '\n'.join(sorted_rules) + '\n'

    # 保存更新后的子文件
    with open(target_file, 'w') as tgt:
        tgt.write(new_content)

if __name__ == '__main__':
    update_list_file('Talkatone.sgmodule', 'TalkatoneAntiAds.list', 'REJECT')
    update_list_file('Talkatone.sgmodule', 'TalkatoneDirect.list', 'Direct')
    update_list_file('Talkatone.sgmodule', 'TalkatoneProxy.list', 'Proxy')
    update_list_file('Talkatone.sgmodule', 'TalkatoneProxyOnly.list', 'Proxy')

import re

def extract_rules_by_keyword(source_file, keyword):
    """
    从母文件中提取包含指定关键词（REJECT/DIRECT/PROXY）的规则，排除注释行。
    """
    with open(source_file, 'r') as f:
        source_content = f.read()

    # 按行分割并筛选出包含指定关键词的规则行，排除注释行
    rules = []
    for line in source_content.split('\n'):
        # 忽略注释行（以 # 开头的行）
        if not line.strip().startswith('#') and keyword in line:
            rules.append(line.strip())

    return rules

def update_list_file(source_file, target_file, keyword):
    """
    更新子文件，使其与母文件中的规则部分保持同步。
    """
    print(f"Updating {target_file} based on {source_file} with {keyword} rules...")
    
    # 从母文件中提取规则
    rules = extract_rules_by_keyword(source_file, keyword)
    if not rules:
        print(f"未找到 {keyword} 规则部分")
        return

    # 读取子文件内容
    with open(target_file, 'r') as f:
        target_content = f.read()

    # 提取子文件中的注释部分
    comment_section = []
    lines = target_content.split('\n')
    for line in lines:
        if line.strip().startswith('#'):
            comment_section.append(line)

    # 保留注释并删除原有规则
    new_content = '\n'.join(comment_section) + '\n\n'

    # 排除 PROXY/DIRECT/REJECT 标签的规则
    new_rules = [rule for rule in rules if 'PROXY' not in rule and 'DIRECT' not in rule and 'REJECT' not in rule]

    # IP 类规则和其他规则分开处理
    ip_rules = []
    other_rules = []

    for rule in new_rules:
        if re.search(r'\d+\.\d+\.\d+\.\d+', rule):  # 判断是否为 IP 类规则
            ip_rules.append(rule)
        else:
            other_rules.append(rule)

    # 添加 no-resolve 标签到 IP 类规则
    ip_rules = [rule + ' ,no-resolve' for rule in ip_rules]

    # 合并规则并排序
    sorted_rules = sorted(other_rules) + sorted(ip_rules)

    # 写入更新后的规则
    new_content += '\n'.join(sorted_rules) + '\n'

    # 保存更新后的子文件
    with open(target_file, 'w') as f:
        f.write(new_content)

if __name__ == '__main__':
    update_list_file('Talkatone.sgmodule', 'TalkatoneAntiAds.list', 'REJECT')
    update_list_file('Talkatone.sgmodule', 'TalkatoneDirect.list', 'DIRECT')
    update_list_file('Talkatone.sgmodule', 'TalkatoneProxy.list', 'PROXY')
    update_list_file('Talkatone.sgmodule', 'TalkatoneProxyOnly.list', 'PROXY')

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

def update_list_file(list_file_path, reject_rules=None, direct_rules=None, proxy_rules=None):
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
    reject_updated = False
    direct_updated = False
    proxy_updated = False

    # 遍历原文件内容
    for line in content:
        # 保留注释行
        if line.startswith('#'):
            updated_content.append(line)
        elif 'DOMAIN-' in line:  # 检测到规则行
            # 如果规则行已经存在并且是 REJECT、DIRECT 或 PROXY 类型，则跳过
            if 'REJECT' in line and reject_rules and not reject_updated:
                updated_content.extend([rule + '\n' for rule in reject_rules])  # 替换 REJECT 规则，并换行
                reject_updated = True
            elif 'DIRECT' in line and direct_rules and not direct_updated:
                updated_content.extend([rule + '\n' for rule in direct_rules])  # 替换 DIRECT 规则，并换行
                direct_updated = True
            elif 'PROXY' in line and proxy_rules and not proxy_updated:
                updated_content.extend([rule + '\n' for rule in proxy_rules])  # 替换 PROXY 规则，并换行
                proxy_updated = True
        else:
            updated_content.append(line)

    # 如果某些类型的规则没有被更新，确保插入它们
    if reject_rules and not reject_updated:
        updated_content.extend([rule + '\n' for rule in reject_rules])  # 添加 REJECT 规则
    if direct_rules and not direct_updated:
        updated_content.extend([rule + '\n' for rule in direct_rules])  # 添加 DIRECT 规则
    if proxy_rules and not proxy_updated:
        updated_content.extend([rule + '\n' for rule in proxy_rules])  # 添加 PROXY 规则

    # 写回更新后的内容
    with open(list_file_path, 'w') as file:
        file.writelines(updated_content)

    print(f"Updated {list_file_path}")  # 日志输出

def update_rule_files():
    """更新所有相关的 .list 文件"""
    module_path = './Talkatone.sgmodule'
    reject_rules, direct_rules, proxy_rules = parse_module_file(module_path)

    # 更新各个 .list 文件
    update_list_file('./TalkatoneAntiAds.list', reject_rules=reject_rules)
    update_list_file('./TalkatoneDirect.list', direct_rules=direct_rules)
    update_list_file('./TalkatoneProxyOnly.list', proxy_rules=proxy_rules)
    update_list_file('./TalkatoneProxy.list', direct_rules=direct_rules, proxy_rules=proxy_rules)

if __name__ == "__main__":
    update_rule_files()

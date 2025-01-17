import os
import re

# 文件路径
module_file = 'Talkatone.sgmodule'
anti_ads_file = 'TalkatoneAntiAds.list'
direct_file = 'TalkatoneDirect.list'
proxy_file = 'TalkatoneProxy.list'
proxy_only_file = 'TalkatoneProxyOnly.list'

# 读取 Talkatone.sgmodule 文件
def read_module_file():
    with open(module_file, 'r') as f:
        return f.readlines()

# 提取规则类型的函数
def extract_rules(lines, rule_type):
    rules = []
    in_block = False
    for line in lines:
        if line.strip().startswith(f'# {rule_type}'):
            in_block = True
        if in_block:
            if line.strip() == "":
                break
            rules.append(line.strip())
    return rules

# 读取子文件并提取现有注释
def read_existing_comments(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    comments = []
    for line in lines:
        if line.strip().startswith('#'):
            comments.append(line.strip())
        else:
            break
    return "\n".join(comments)

# 写入更新后的规则文件
def write_file(file_path, rules, existing_comments):
    with open(file_path, 'w') as f:
        # 保留子文件中的现有注释，并在其下方添加空行和新规则
        f.write(existing_comments)
        f.write("\n\n")  # 保证注释后有空行
        for rule in rules:
            f.write(rule + "\n")

# 去除重复规则并进行排序
def process_rules(rules):
    unique_rules = list(dict.fromkeys(rules))  # 去除重复规则
    return unique_rules

# 处理规则类型并更新子文件
def process_module_file():
    lines = read_module_file()

    # 提取不同类型的规则
    reject_rules = extract_rules(lines, 'RECJECT')
    direct_rules = extract_rules(lines, 'Direct')
    proxy_rules = extract_rules(lines, 'Proxy')
    proxy_only_rules = extract_rules(lines, 'ProxyOnly')

    # 处理每个规则并排序（IP类规则排在末尾）
    reject_rules = process_rules(reject_rules)
    direct_rules = process_rules(direct_rules)
    proxy_rules = process_rules(proxy_rules)
    proxy_only_rules = process_rules(proxy_only_rules)

    # 读取子文件中的现有注释
    anti_ads_comments = read_existing_comments(anti_ads_file)
    direct_comments = read_existing_comments(direct_file)
    proxy_comments = read_existing_comments(proxy_file)
    proxy_only_comments = read_existing_comments(proxy_only_file)

    # 更新规则到对应的文件，保留原有注释
    write_file(anti_ads_file, reject_rules, anti_ads_comments)
    write_file(direct_file, direct_rules, direct_comments)
    write_file(proxy_file, proxy_rules, proxy_comments)
    write_file(proxy_only_file, proxy_only_rules, proxy_only_comments)

if __name__ == '__main__':
    process_module_file()

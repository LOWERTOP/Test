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

# 写入更新后的规则文件
def write_file(file_path, rules, comment):
    with open(file_path, 'w') as f:
        f.write(comment)
        f.write("\n\n")
        for rule in rules:
            f.write(rule + "\n")

# 获取注释内容
def extract_comment(lines):
    comment = []
    for line in lines:
        if line.strip().startswith('#'):
            comment.append(line.strip())
        else:
            break
    return "\n".join(comment)

# 去除重复规则并进行排序
def process_rules(rules):
    unique_rules = list(dict.fromkeys(rules))  # 去除重复规则
    return unique_rules

# 处理规则类型
def process_module_file():
    lines = read_module_file()

    # 提取注释
    comment = extract_comment(lines)

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

    # 更新规则到对应的文件
    write_file(anti_ads_file, reject_rules, comment)
    write_file(direct_file, direct_rules, comment)
    write_file(proxy_file, proxy_rules, comment)
    write_file(proxy_only_file, proxy_only_rules, comment)

if __name__ == '__main__':
    process_module_file()

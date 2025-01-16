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

def update_list_file(list_file_path, rules):
    # 直接写入新的规则内容
    with open(list_file_path, 'w') as file:
        file.write("# Rules\n")  # 加入规则头注释
        file.write(rules)  # 写入规则

    print(f"Updated {list_file_path}")  # 日志输出

def update_rule_files():
    module_path = './Talkatone.sgmodule'
    reject_rules, direct_rules, proxy_rules = parse_module_file(module_path)

    # 构造规则内容
    reject_rules_str = "\n".join(reject_rules)
    direct_rules_str = "\n".join(direct_rules)
    proxy_rules_str = "\n".join(proxy_rules)

    # 更新 .list 文件
    update_list_file('./TalkatoneAntiAds.list', reject_rules_str)
    update_list_file('./TalkatoneDirect.list', direct_rules_str)
    update_list_file('./TalkatoneProxyOnly.list', proxy_rules_str)
    update_list_file('./TalkatoneProxy.list', "\n".join(reject_rules + direct_rules + proxy_rules))

if __name__ == "__main__":
    update_rule_files()

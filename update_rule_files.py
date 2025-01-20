import re

# 父文件和子文件的路径
parent_file_path = 'Talkatone.sgmodule'
child_files = [
    'TalkatoneAntiAds.list',
    'TalkatoneProxy.list',
    'TalkatoneDirect.list',
    'TalkatoneProxyOnly.list'
]

def extract_rules(content):
    """从内容中提取规则部分"""
    start = content.find('[Rule]')
    if start == -1:
        return ''
    
    # 从 [Rule] 开始到文件末尾的内容
    rules = content[start:]
    return rules

def filter_rules(rules, include_ip=False):
    """过滤规则，保留特定策略的规则"""
    filtered_rules = []
    for line in rules.splitlines():
        if "IP-CIDR" in line and include_ip:
            filtered_rules.append(line)
        elif "IP-CIDR" not in line and not include_ip:
            # 移除策略部分
            line = re.sub(r",(REJECT-DROP|PROXY|DIRECT)", "", line)
            filtered_rules.append(line)
    return "\n".join(filtered_rules)

def update_child_file(child_file_path, filtered_rules):
    """更新子文件的规则部分，保留注释内容"""
    with open(child_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 提取注释内容，假设注释部分在文件开头
    comments = re.findall(r'^(#.*\n)+', content)
    comments = comments[0] if comments else ''
    
    # 保留注释内容并写入文件
    final_content = comments + filtered_rules + '\n'
    with open(child_file_path, 'w', encoding='utf-8') as file:
        file.write(final_content)

def main():
    with open(parent_file_path, 'r', encoding='utf-8') as file:
        parent_content = file.read()
    
    # 提取父文件的规则部分
    parent_rules = extract_rules(parent_content)
    
    # 更新每个子文件
    for child_file in child_files:
        include_ip = "Direct" in child_file or "Proxy" in child_file  # 判断是否包含 IP 类规则
        filtered_rules = filter_rules(parent_rules, include_ip)
        update_child_file(child_file, filtered_rules)

if __name__ == '__main__':
    main()

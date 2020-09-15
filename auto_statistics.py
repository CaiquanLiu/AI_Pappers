# coding=utf-8
"""
paper 统计
"""

import os

files_list = os.listdir('./')

markdown_files_list = list()

for file in files_list:
    if os.path.splitext(file)[1] == '.md':
        markdown_files_list.append(file)

markdown_files_list.remove('README.md')
markdown_files_list.remove('模板.md')

statistic_info = list()
all_papers_count = 0
for file in markdown_files_list:
    file_name = os.path.splitext(file)[0]

    f = open(file, 'r', encoding='UTF-8')
    lines = f.readlines()
    papaper_count = 0
    for line in lines:
        table_elements = line.split('|')
        for element in table_elements:
            element = element.strip()
            if element.startswith('《') and element.endswith('》'):
                papaper_count += 1
                all_papers_count += 1
                break
    f.close()

    file_info = {file_name: papaper_count}
    statistic_info.append(file_info)

for item in statistic_info:
    print(item)

print('all papers count: {}'.format(all_papers_count))

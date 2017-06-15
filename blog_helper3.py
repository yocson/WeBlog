# -*- coding: utf-8 -*-

import time
import sys
import codecs
import yaml


def add_yaml(in_file, parameters, out_file):
    # 打开源文件
    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()

    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


    yaml_dict = {
        "layout": "post",
        "date": date,
        "author": 'Yocson',
    }

    yaml_dict = dict(yaml_dict, **parameters)

    # 生成yaml文本
    yaml_text = yaml.dump(yaml_dict, encoding='utf-8', default_flow_style=False)
    print(yaml_text)
    # 与源文本合并
    text = '---\n' + yaml_text.decode("unicode-escape") + '---\n' + text

    # 目标文本名字
    file_name = time.strftime("%Y-%m-%d", time.localtime()) + '-' + out_file

    blog_path = '/Users/KSH/Library/Mobile Documents/com~apple~CloudDocs/AlanKSH.github.io/_posts/'
    # 输出成目标文本
    output_file = codecs.open(blog_path+file_name+".md", mode='w', encoding="utf8")
    output_file.write(text)

    input_file.close()
    output_file.close()


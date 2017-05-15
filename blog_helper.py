# -*- coding: utf-8 -*-

import codecs
import yaml
import time
import sys



def add_yaml(in_file):
    # 打开源文件
    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()

    # 询问输入
    title = input("TITLE?")
    subtitle = input("SUBTITLE?")
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    img = input("IMG?")
    tag = []
    tag.append(input("TAG1?"))
    tag.append(input("TAG2?"))

    yaml_dict = {
        "layout": "post",
        "title": "%s" %title,
        "subtitle": "%s" %subtitle,
        "date": date,
        "author": 'Yocson',
        "header-img": "img/%s.jgp" %img,
        "tags": tag
    }

    # 生成yaml文本
    yaml_text = yaml.dump(yaml_dict,default_flow_style=False)
    # 与源文本合并
    text = '---\n' + yaml_text + '---\n' + text

    # 目标文本名字
    file_title = input("FILE_TITLE(EN)?")
    file_name = time.strftime("%Y-%m-%d", time.localtime()) + '-' + file_title

    # 输出成目标文本
    output_file = codecs.open(file_name+".md", mode='w', encoding="utf-8")
    output_file.write(text)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    in_file = sys.argv[1]
    print(in_file)
    add_yaml(in_file)

# -*- coding: utf-8 -*-
"""GUI界面传入参数，增加YAML"""

import time
import sys
import codecs
import yaml


def add_yaml(in_file, out_dir, parameters, out_file):
    # 打开源文件
    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()

    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    yaml_dict = {
        "layout": "post",
        "date": date,
    }

    yaml_dict = dict(yaml_dict, **parameters)

    # 生成yaml文本
    yaml_text = yaml.dump(yaml_dict, encoding='utf-8', default_flow_style=False)
    print(yaml_text)
    # 与源文本合并
    text = '---\n' + yaml_text.decode("unicode-escape") + '---\n' + text

    # 目标文本名字
    file_name = time.strftime("%Y-%m-%d", time.localtime()) + '-' + out_file

    # 输出成目标文本
    output_file = codecs.open(out_dir + '/' + file_name + ".md", mode='w', encoding="utf8")
    output_file.write(text)

    input_file.close()
    output_file.close()


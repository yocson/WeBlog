# -*- coding: utf-8 -*-
"""增加YAML并且将图片上传至七牛云，GUI交互"""

import time
import sys
import codecs
import yaml
from qiniu import Auth
from qiniu import BucketManager, put_file, etag
import config


def blog_helper(in_file, out_dir, parameters, out_file):
    # 打开源文件
    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.readlines()

    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    yaml_dict = {
        "layout": "post",
        "date": date,
    }

    yaml_dict = dict(yaml_dict, **parameters)

    # 生成yaml文本
    yaml_text = yaml.dump(yaml_dict, encoding='utf-8', default_flow_style=False)
    print(yaml_text)

    # yaml文本前后增加---
    yaml_text = '---\n' + yaml_text.decode("unicode-escape") + '---\n'

    # 目标文本名字
    file_name = time.strftime("%Y-%m-%d", time.localtime()) + '-' + out_file

    # 开始分析图片
    count = 0
    img_list = []
    new_text = ''

    for line in text:
        # 判断是否是图片
        if line[0:2] == '![':
            # 本地地址加入待上传列表
            img_list.append(line.split('(')[1].split(')')[0])
            # 生成新的图片格式
            line = '![%d](%s%s/%d.png)\n'\
            %(count, config.LINK_DOMAIN, file_name.split('.')[0], count)
            count += 1
        # 加入新的输出文本中
        new_text += line

    # 上传图片
    upload_imgs(img_list, file_name)

    # 输出成目标文本
    output_file = codecs.open(out_dir + '/' + file_name + ".md", mode='w', encoding="utf8")
    output_file.writelines(yaml_text)
    output_file.writelines(new_text)

    input_file.close()
    output_file.close()

def upload_imgs(img_list, file_name):
    access_key = config.ACCESS_KEY
    secret_key = config.SECRET_KEY

    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)

    bucket_name = config.BUCKET_NAME

    for index, img in enumerate(img_list):
        key = '%s/%d.png'%(file_name.split('.')[0], index)
        token = q.upload_token(bucket_name, key, 3600)
        localfile = img

        ret, info = put_file(token, key, localfile)
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)

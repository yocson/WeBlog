# -*- coding: utf-8 -*-

import sys
import codecs
from qiniu import Auth
from qiniu import BucketManager, put_file, etag
import config

def qiniu_update(file_source, out_dir):
    input_file = codecs.open(file_source, 'r', 'utf8')
    text = input_file.readlines()

    file_name = file_source.split('/')[-1]

    count = 0
    img_list = []

    input_file.close()

    output_file = codecs.open(out_dir + '/' + file_name, 'w', 'utf8')
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

    output_file.writelines(new_text)
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

if __name__ == "__main__":
    file_name = sys.argv[1]
    qiniu_update(file_name)

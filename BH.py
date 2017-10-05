import sys
import time
import codecs
import yaml
import config
from qiniu import Auth
from qiniu import BucketManager, put_file, etag


class BlogHelper:
    def __init__(self, file_name, des_dirname, parameter_list, new_filename):
        self.file_name = file_name
        self.des_dirname = des_dirname
        self.parameter_list = parameter_list
        self.new_filename = new_filename

    def readfile(self, in_file):
        input_file = codecs.open(in_file, mode="r", encoding="utf-8")
        text = input_file.readlines()
        input_file.close()
        return text

    def writefile(self, yaml_text, new_text):
        output_file = codecs.open(self.des_dirname + '/' + self.new_filename + ".md", mode='w', encoding="utf8")
        output_file.writelines(yaml_text)
        output_file.writelines(new_text)

        output_file.close()

    def uploadimages(self, text):
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
                %(count, config.LINK_DOMAIN, self.file_name.split('.')[0], count)
                count += 1
            # 加入新的输出文本中
            new_text += line

        access_key = config.ACCESS_KEY
        secret_key = config.SECRET_KEY

        q = Auth(access_key, secret_key)
        bucket = BucketManager(q)

        bucket_name = config.BUCKET_NAME

        for index, img in enumerate(img_list):
            key = '%s/%d.png'%(self.file_name.split('.')[0], index)
            token = q.upload_token(bucket_name, key, 3600)
            localfile = img

            ret, info = put_file(token, key, localfile)
            assert ret['key'] == key
            assert ret['hash'] == etag(localfile)

    def addyaml(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        yaml_dict = {
            "layout": "post",
            "date": date,
        }

        yaml_dict = dict(yaml_dict, **self.parameter_list)

        # 生成yaml文本
        yaml_text = yaml.dump(yaml_dict, encoding='utf-8', default_flow_style=False)
        print(yaml_text)

        # yaml文本前后增加---
        yaml_text = '---\n' + yaml_text.decode("unicode-escape") + '---\n'

        # 目标文本名字
        self.new_filename = time.strftime("%Y-%m-%d", time.localtime()) + '-' + self.new_filename


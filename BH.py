"""
This module contains a BlogHelper class
"""
import time
import codecs
import yaml
import config
from qiniu import Auth
from qiniu import BucketManager, put_file, etag

class BlogHelper(object):
    """Add YAML or Upload Images or Do Both"""
    def __init__(self, file_name, des_dirname, parameter_list, new_filename, key_list):
        """
        Constructor
        :param file_name: file name with path
        :param des_dirname: where the file is stored after operation
        :param parameter_list: all YAML parameters
        :param new_filename:  new file name
        """
        self.file_name = file_name
        self.des_dirname = des_dirname
        self.parameter_list = parameter_list
        self.new_filename = time.strftime("%Y-%m-%d", time.localtime()) + '-' + new_filename
        self.ACCESS_KEY = key_list[0]
        self.SECRET_KEY = key_list[1]
        self.LINK_DOMAIN = key_list[2]
        self.BUCKET_NAME = key_list[3]

    def readfile(self):
        """
        Read file into a list line by line
        :param in_file: file path
        """
        input_file = codecs.open(self.file_name, mode="r", encoding="utf-8")
        text = input_file.readlines()
        input_file.close()
        return text

    def writefile(self, yaml_text, new_text, useOriname):
        """
        write file to destination
        :param yaml_text: yaml
        :param new_text: all new text
        """
        if (useOriname):
            output_file = codecs.open(self.file_name, mode='w', encoding="utf8")
        else:
            output_file = codecs.open(self.des_dirname + '/' + self.new_filename + ".md", mode='w', encoding="utf8")
        output_file.writelines(yaml_text)
        output_file.writelines(new_text)

        output_file.close()

    def uploadimages(self, text = []):
        """
        test images and then upload using qiniu API
        :param text: all text line by line
        :returns: new_text
        """
        if text == []:
            return []

        # count images number
        count = 0
        img_list = []
        new_text = ''

        for line in text:
            # check whether this line is a image or not
            if line[0:2] == '![':
                # capture local path and save it to to-upload list
                img_list.append(line.split('(')[1].split(')')[0])
                # for everyline create a new image URL based on order
                line = '![%d](%s%s/%d.png)\n'\
                %(count, self.LINK_DOMAIN, self.file_name.split('.')[0].split('/')[-1], count)
                count += 1
            # add back to new text list(wash original text)
            new_text += line

        access_key = self.ACCESS_KEY
        secret_key = self.SECRET_KEY

        q = Auth(access_key, secret_key)
        bucket = BucketManager(q)

        bucket_name = self.BUCKET_NAME

        for index, img in enumerate(img_list):
            key = '%s/%d.png'%(self.file_name.split('.')[0].split('/')[-1], index)
            token = q.upload_token(bucket_name, key, 3600)
            localfile = img

            ret, info = put_file(token, key, localfile)
            assert ret['key'] == key
            assert ret['hash'] == etag(localfile)

        return new_text

    def addyaml(self):
        """
        add YAML to form yamltext
        :returns: yaml_text
        """
        # create date info
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # yaml dict with two basic info
        yaml_dict = {
            "layout": "post",
            "date": date,
        }

        # add user yaml info into dict
        yaml_dict = dict(yaml_dict, **self.parameter_list)

        # transfer dict to yaml text
        yaml_text = yaml.dump(yaml_dict, encoding='utf-8', default_flow_style=False)
        print(yaml_text)

        # add '---' before and after YAML text
        yaml_text = '---\n' + yaml_text.decode("unicode-escape") + '---\n'

        return yaml_text

if __name__ == '__main__':
    PARA_LIST =  {'title': "fdf",
                 'subtitle': "sdfsdf",
                 'header-img': "asdfd",
                 'author': "sdfasdf"
                 }
    bH = BlogHelper("/Users/KSH/Desktop/tessst.md", "/Users/KSH/Desktop", PARA_LIST, "testttt")
    original_text = bH.readfile()
    yaml_text = bH.addyaml()
    text_after_up = bH.uploadimages(original_text)
    bH.writefile(yaml_text, text_after_up)


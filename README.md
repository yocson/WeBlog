# Jekyllblog_helper
用于生成带有YAML头信息的Jekyll博客文件

相关博文：

- [快速生成符合Jekyll格式的博客*一：移动端 - Ehurdas's Blog](http://yocson.com/2017/05/15/jekyllblogh1/)
- [快速生成符合Jekyll格式的博客*二 ：电脑端 - Ehurdas's Blog](http://yocson.com/2017/05/16/jekyllblogh2/)

## 用法：
python blog_helper.py \<file>

## 生成：
```YAML
---
layout:     post
title:      ""
subtitle:   ""
date: 
author: ""
header-img: "img/.jpg"
tags:
---
```
带有以上YAML信息，输出符合jekyll文件名的博客文件

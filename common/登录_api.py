#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Time : 2022/10/18 19:40
# @File : 登录_api.py
# @Software: PyCharm

from data.read_yaml import get_yaml
import requests
import pprint #完美打印
import json

#封装请求的类
class Login():
    def denglu(self,inData):
        #url路径
        url = 'http://192.168.10.7:9091/api/v1/user/login'
        #请求参数
        payload = json.dumps(inData)
        #发送请求
        """
        参数方式
        data----一般是表单格式
        json----json
        files----文件上传接口
        params----参数会放进url路径里 ?a=1&b=2
        """
        res = requests.post(url,data=payload)

        # 读取响应
        # print(res.text)  #以文本方式读取
        # print(res.json())  # 以字典方式读取
        # print(res.content)  #以字节方式读取
        # return res.text  #json---字符串
        return res.json()  #获取响应数据


if __name__ == '__main__':   #快捷   键ctrl+j
    login = Login()  #实例化对象
    resp = login.denglu({'authRequest': {'userName': 'user01', 'password': 'pwd'}})
    # print(resp)
    pprint.pprint(resp)


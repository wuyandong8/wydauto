# -*- coding: UTF-8 -*-
# @date: 2020/6/14 23:19
# @name: requests1
# @author：wuyandong
import requests


def get_one():
    data = {
        'name': 'germey',
        'age': 22
    }
    res = requests.get("https://www.baidu.com/", params=data)
    print(res.headers)
    print(type(res.text), type(res.content))


if __name__ == '__main__':
    get_one()
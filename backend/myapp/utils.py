#coding=utf8
import json
import os
import urllib.request
import sys
import importlib
importlib.reload(sys)
# reload(sys)

class DoubanBook(object):
    def __init__(self, bookname):
        self.imgdir = '/tmp/imgtmp/image/'
        self.url = 'https://api.douban.com/v2/book/search?q=%s&count=1' % bookname
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
    def get_detail(self):
        request = urllib.Request(self.url, headers=self.headers)
        response = urllib.urlopen(request)
        ret = response.read()
        retdict = eval(ret)
        img = retdict['books'][0]['image'].replace('\\','')
        if not os.path.isdir(self.imgdir):
            os.makedirs(self.imgdir)
        res = urllib.urlopen(img)
        with open('%s%s' % (self.imgdir, img.split('/')[-1]), 'wb') as f:
            f.write(res.read())
        return json.loads(ret)

class IdcData(object):
    def __init__(self):
        self.treedata = [
            {
                    'id':1,
                    'title': 'IDC资产',
                    'autotype': 'IDC',
                    'expand': 'true',
                    'children': [
                        {
                            'id':2,
                            'title': '亦庄机房',
                            'autotype': 'idc',
                            'expand': 'true',
                            'children': [
                                {
                                    'id':3,
                                    'title': '机柜01',
                                    'autotype': 'rack'
                                },
                                {
                                    'id':4,
                                    'title': '机柜02',
                                    'autotype': 'rack'
                                }
                            ]
                        },
                        {
                            'id':5,
                            'title': '网宿',
                            'autotype': 'idc',
                            'expand': 'true',
                            'children': [
                                {
                                    'id':6,
                                    'title': '网宿01',
                                    'autotype': 'rack',
                                },
                                {
                                    'id':8,
                                    'title': '网宿02',
                                    'autotype': 'rack',

                                }
                            ]
                        }
                ]
            }
        ]

    def gettree(self):
        return self.treedata



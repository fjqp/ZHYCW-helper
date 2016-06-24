#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from PIL import Image, ImageFilter, ImageEnhance
from StringIO import StringIO
import pytesser


class ImageUtil:
    @staticmethod
    def two_value_m1(i):
        '''二值化 '''
        i = i.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(i)
        i = enhancer.enhance((2))
        i = i.convert('1')
        return ib

    @staticmethod
    def convert_to_gray_png(i):
        '''转换到灰度图'''
        i = i.convert('L')
        return i

class ZHYCW:
    LOGIN_URL_GET = 'http://passport.chinahr.com/pc/tologin?backUrl=http://www.chinahr.com/shenzhen/'
    LOGIN_URL_POST = 'http://passport.chinahr.com/ajax/pc/login'

    def __init__(self):
        self.s = requests.Session()

    def login(self):
        r = self.s.get(ZHYCW.LOGIN_URL_GET)
        print r.text
        r = self.s.get('http://passport.chinahr.com/m/genpic')
        i = Image.open(StringIO(r.content))
        i.show()

        imgCode = pytesser.image_to_string(i)
        print '-->', imgCode
        
        params = {
            'backUrl': "http://www.chinahr.com/shenzhen/",
            'from': '',
            'imgCode': imgCode,
            'input': '15728567842',
            'pwd': "31af4a634cf808c8a7572b741dec6234b751165471560d368e4dd8fb84428c3db240c478a9d1afb455c9\
            e5235d84dd51bdc8ddf1fc621b3b0d4a10664ff13cd3846804a242d0cb7fab7a88f82d9e71ae6bc815d0191691\
            532bfd45c8ee3955250f17b50d16e76c937ab7de4a0aa4ae1040ee50465a45c753e2a8909016a04291",
            'rember': '1'
        }

        r = self.s.post(ZHYCW.LOGIN_URL_POST, data=params)
        print r.text

if __name__ == '__main__':
    ZHYCW().login()

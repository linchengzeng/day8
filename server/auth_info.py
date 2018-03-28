# -*- coding:utf-8 -*-
#  Author:aling

import xml.etree.ElementTree as ET

class Auth_user_info(object):

    def auth_login_info(self,user_id, user_pwd):
       tree = ET.parse('userinfo.xml')   #打开xml文件并解析它
       root = tree.getroot()   #获取根节点  users
       for child in root:  #  遍历得到各用户总信息
           child.attrib
           if child.attrib.get('id') == user_id and child.attrib.get('pwd') == user_pwd:
               print('file in auth_info.py')
               print('user auth success')
               return 'Success'
           else:
               print('auth_info.py line 15')
               return 'Fail'

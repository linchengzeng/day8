# -*- coding:utf-8 -*-
#  Author:aling


def authencation(func):
    def wapper(*args,**kwargs):
        user_name = input('请输入用户名：')
        user_pwd = input('请输入密码：')
        auth_result = auth_info.Auth_user_info(user_name,user_pwd)
        if auth_result == 'Success':
            global user_data
            user_data = {
                'userid': None,
                'userpwd': None,
            }
            global user_home
            user_home = base_path + '/client_files/' + user_data['userid']  # 用户根目录
            func
        else:
            print('authencation Fail')
            print('please clicket your userid and password!')
            return None
    return wapper

@authencation
def Ftp_main():
    print('this is ftp main')
    Ftp_Client_Start()


Ftp_main
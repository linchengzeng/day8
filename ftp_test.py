# -*- coding:utf-8 -*-
#  Author:aling
# import os
# #
# # print(os.path.dirname(__file__))
# # print(os.path.abspath(__file__))
# # print(os.path.basename(__file__))
#
# base_path = os.path.dirname(__file__)
# user_data = {
#     'userid':'admin',
#     'userpwd':'admin',
# }
#
# user_home = base_path + '\\' + user_data['userid'] + '\\'  # 用户根目录
# # print(user_home)
# file_path = base_path + '\\server_files\\' + '01.mp4'
# print(file_path)

# bat = b'session'
# print(bat)


# with open(file_path, 'rb') as f:
#     while f_size - sended_size > 0:
#         contest = f.read(204800)   #将要发送的内容大小：
#         conn.send(contest)  # 发送本次读取到的信息
#         sended_size += len(contest)
#         f.seek(sended_size)  # 将光标句柄移至已发送的位置（即从光标开始往后都是未发送的内容)
#     print('文件发送完毕！')
#     conn.send(b'send_session')
# ###############################################################
# f_size = 0  #已接收文件大小
#     while True:
#         data = f_client_conn.recv(204800)
#         with open(user_home+'/'+f_name, 'ab+') as f:
#             f.write(data)
#             f.flush()
#             f_size += len(data)
#         if not len(data): break
#     print('文件接收完毕')
# print("##################################################################")
import os,subprocess,sys,platform
result = os.popen('ls').readlines()
result = os.system('dir')
result = sys.getdefaultencoding()
result = subprocess.call('dir',shell=True)#  shell在windows中必须添加
print(result)

'''
    python中，platform模块给我们提供了很多方法去获取操作系统的信息
    如：
        import platform
        platform.platform()        #获取操作系统名称及版本号，'Linux-3.13.0-46-generic-i686-with-Deepin-2014.2-trusty'  
        platform.version()         #获取操作系统版本号，'#76-Ubuntu SMP Thu Feb 26 18:52:49 UTC 2015'
        platform.architecture()    #获取操作系统的位数，('32bit', 'ELF')
        platform.machine()         #计算机类型，'i686'
        platform.node()            #计算机的网络名称，'XF654'
        platform.processor()       #计算机处理器信息，''i686'
        platform.uname()           #包含上面所有的信息汇总，('Linux', 'XF654', '3.13.0-46-generic', '#76-Ubuntu SMP Thu Feb 26 18:52:49 UTC 2015', 'i686', 'i686')

        还可以获得计算机中python的一些信息：
        import platform
        platform.python_build()
        platform.python_compiler()
        platform.python_branch()
        platform.python_implementation()
        platform.python_revision()
        platform.python_version()
        platform.python_version_tuple()
'''
# result2 = platform.platform()
# print(result2)
# a = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# k1 = [x for x in a if x > 66]
# k2 = [y for y in a if y <= 66]
# dict1 = {'aa':k1,'bb':k2}
# # print(dict1)
# for key in dict1:
#     print(key,':',dict1[key])
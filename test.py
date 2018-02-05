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
print("##################################################################")
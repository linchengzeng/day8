# -*- coding:utf-8 -*-
#  Author:aling
##########   例一  ##############
# while True:
#     # 等电话打进来,
#     # 若有来电，则标记该来电
#     # 1、conn链接的标记位（就是客户端连接过来而在服务器端为其生成的一个连接实例）
#     # 2、addr对方的地址
#     print('接收到来电，正在接通中……')
#     conn, addr = s_server.accept()
#
#     while True:
#         c_data = conn.recv(1024)  # 收信息
#         if not c_data:
#             print('client has lost……')
#             break   # 若客户端断开，则跳出循环
#         conn.send(c_data.upper())  # 发信息(将接收到的数据全部变成大写)
#         print('sever_resend:',c_data)
# s_server.close()


##########   例二  ##############
# c_conn, c_addr = s_server.accept()
# print('接收到客户端请求，正在等待传输数据……')
# while True:
#
#     c_data = c_conn.recv(1024)
#     if not c_data: break
#     c_file = open(time())
#     c_data = c_file.read()
#
# s_server.close()



'''
  客户端 部分

'''


##############  例一  中文传输  ###############
# while True:
#     f = input('请输入您要上传的文件路径(如E:\\ABC\\D.TXT)>>:').encode('utf-8')
#     if f == 'exit':
#         f_client.close()  # 关闭连接
#         exit()
#     if len(f) == 0:continue   # 不能发空数据，否则服务器会认为发送数据未结束
#     f_client.send(f)  # 发信息 #python3要求发送的必须为byte类型的数据
#     data = f_client.recv(1024)  # 1024字节
#     print("client_recv:",data.decode())  # bytes类型转回中文要decode
#
# f_client.close()  # 关闭连接


##########   例二  传输命令  ##############
# while True:
#     user_input_fle = input('请输入您要上传的文件路径(如E:\\ABC\\D.TXT)>>:')
#     if user_input_fle == 'exit': f_client.close(), exit()
#     if len(user_input_fle) == 0: continue
#     upload_file = open(user_input_fle, 'rb')
#     f_client.sendall(upload_file)
#     f_s_recv = f_client.recv(1024)
#     print(f_s_recv.decode())
# f_client.close()

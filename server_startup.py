# -*- coding:utf-8 -*-
#  Author:aling
# 服务器端
import socket,os,subprocess,re

s_server = socket.socket()  # 声明socket类型（地址族、协议类型等 ），同时生成socket连接对象
Host_ip = '127.0.0.1'  #服务器端服务所绑定使用的IP
Ip_port = 8823
s_server.bind((Host_ip, Ip_port))  # 绑定要监听的端口

# while True:
s_server.listen(5)  # 最多挂起5个连接   此部分在异步的情况下才能试出效果
base_path = os.path.dirname(__file__)  # 文件所在目录
user_data = {
    'userid': 'admin',
    'userpwd': 'admin',
}
user_home = base_path + '/server_files/' + user_data['userid']  # 用户根目录
user_in_path = user_home
#######      例三     ##############

class Ftp_server_start(object):

    def __init__(self):
        print('server line 57')
        self.start()

    def start(self):
        print('this is server start line 55')
        ftp_server_menu = {
            'get_file': self.get_file,
            'show_files':self.show_files,
            'put_file':self.put_files,
            'cd_files':self.cd_files
        }
        # def __init__(self):
        #     Ftp_server_start
        # if c_data== 'get_file':
        #     print('客户端发过来的请求为：get_file')
        ftp_server_menu[c_data]()

    # 文件下载
    def get_file(self):
        print('this is ftp server line 72')
        f_name = conn.recv(204800)
        print('从客户端发过来的请求下载的文件名称：%s'%f_name)
        file_path = base_path + '/server_files/' + f_name.decode('utf-8')
        print(file_path)
        if os.path.exists(file_path):
            f_size = os.path.getsize(file_path)  # 文件大小
            print('被请求文件大小',f_size)
            conn.send(str(f_size).encode('utf-8'))  # 发送file_exist 表示文件存在并开始传送文件
            send_break = conn.recv(204800).decode('utf-8') # 接收到send_break表示客户端文件存在
            print('send_break:',send_break)
            if send_break == 'send_break':
                print('客户端出错')
                return None
            sended_size = 0    # 已发送文件大小
            # conn.send('abcdefg'.encode('utf-8'))
            i = 0
            with open(file_path, 'rb') as f:
                while f_size - sended_size >= 204800:
                    print('文件大小：', f_size)
                    # print('未发送文件大小：', f_size - sended_size)
                    # print('读取前光标句柄所在位置：', f.tell())
                    if f_size - sended_size > 204800:
                        contest = f.read(204800)
                    else:
                        contest = f.read(f_size - sended_size)
                    # print('将要发送的内容大小：', len(contest))
                    conn.send(contest)  # 发送本次读取到的信息
                    sended_size += len(contest)
                    f.seek(sended_size)  # 将光标句柄移至已发送的位置（即从光标开始往后都是未发送的内容)
                    # print('光标句柄所在位置：', f.tell())
                    i += 1
                    print('发送了:', i, '次')
                    print('已发送文件大小：', sended_size)
                else:
                    print('准备发送最后一次')
                    print('读取前光标句柄所在位置：', f.tell())
                    print('剩余文件大小',f_size - sended_size)
                    contest = f.read(f_size - sended_size)
                    print('contest len:',len(contest))
                    conn.sendall(contest)
                    # conn.send(b'send_session')
                    print('文件发送完毕！')
                    # conn.send(b'send_session')
                # return self.start()
        else:
            conn.send('file_error'.encode('utf-8'))
            return None

    # 文件列表
    def show_files(self):
        print('this is show files')
        file_list = os.listdir(user_in_path)
        print(file_list)
        file_dict = {}
        for element in file_list:
            if os.path.isfile(user_in_path +'/'+element):
                print('文件:',element)
                file_dict[element] = '文件'
            elif os.path.isdir(user_in_path +'/'+element):
                print('目录:',element)
                file_dict[element] = '文件夹'
            elif element == '.git':continue
            elif element == '.idea':continue
        print(file_dict)
        conn.send(str(file_dict).encode('utf-8'))

    def put_files(self):
        print('this is put files line 100')
        put_file = conn.recv(204800).decode('utf-8')
        if put_file == 'client_file_error':
            print('客户端出错！')
            return None
        put_file_size = conn.recv(204800).decode('utf-8')
        file_name = re.split('\\\\', put_file)[-1]
        print('客户端请求上传文件名称：', re.split('\\\\', file_name)[-1])
        print('客户端请求上传文件大小：',put_file_size)
        # 开始判断服务器是否存在同名文件

        if os.path.exists(user_in_path+'/'+file_name):
            print('服务端出错，请检查后再传输!')
            conn.send('put_break'.encode('utf-8'))
        else:
            conn.send('ckeck_success'.encode('utf-8'))
            print('start put file line 110')
            f_size = 0  # 已上传文件的大小
            while int(put_file_size) - f_size > 0:  # 大于小表示文件未传输完毕
                data = conn.recv(204800)  # 服务传输过来的文件块数据
                with open(user_in_path + '/' + file_name, 'ab+') as f:
                    f.write(data)
                    f.flush()
                    f_size += len(data)
                    print('已接收：', f_size)
            else:
                print('文件接收完毕')



    def cd_files(self):
        global user_in_path
        print('this is cd files line 144')
        self.show_files()
        cd_files_str = conn.recv(204800).decode('utf-8')
        print('cd_files_str:%s'%cd_files_str)
        print('cd_files_str:%s'%type(cd_files_str))
        if cd_files_str == str('..'):
            print('abc')
            print('user_in_old_path:',user_in_path)
            user_new_in_path = os.path.dirname(user_in_path)
            print('user_in_new_path',user_new_in_path)
            user_in_path = user_new_in_path
            self.show_files()
        elif os.path.exists(user_in_path+ '/' + cd_files_str):
            print('新目录：',user_in_path+ '/' + cd_files_str)
            user_in_path = user_in_path+ '/' + cd_files_str
            self.show_files()
        else:print('不知所云')



while True:
    print('已经开始监听端口，现在正在等电话打进来……')

    conn, addr= s_server.accept()   # 标记客户端连接conn,标记客户端地址addr
    # 开始验证
    # user_name = conn.recv(204800)
    # pass_word = conn.recv(204800)
    # if user_name == user_data['userid'] and pass_word == user_data['userpwd']:
    #     # 通过验证
    #     pass

    while True:
        print('接收到客户端请求，正在等待传输数据……')
        c_data = conn.recv(204800).decode('utf-8')
        print('收到客户端请求为:',c_data)
        if c_data == 'exits':
            conn.close()
            print('客户断开连接！正在等待新的连接……')
            break
        Ftp_server_start()

s_server.close()
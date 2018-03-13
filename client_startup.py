# -*- coding:utf-8 -*-
#  Author:aling
# 客户端
import socket,os


f_client_conn = socket.socket()
h = '127.0.0.1'   #服务器端IP
p = 8823
f_client_conn.connect((h, p))



#######      例三   文件传输  ##############
base_path = os.path.dirname(__file__)  # 文件所在目录
user_data = {
    'userid':'admin',
    'userpwd':'admin',
}

user_home = base_path + '/client_files/' + user_data['userid']  # 用户根目录
print('client user home:',user_home)
# print('测试FTP传输文件1')
class Ftp_Client_Start(object):
    def __init__(self):
        # print('this is client_startup.py' in line 51)
        self.start()

    def start(self):
        ftp_menu = '''
            show：显示当前文件夹下的所有文件及文件详细信息
            put：上传文件
            get：下载文件
            cd：切换目录
            exits：退出程序
            
        '''
        while True:
            print(ftp_menu)
            user_input = input('请输入需要的操作：')
            self.user_main_page(user_input)


    def user_main_page(self,user_input):
        # print('this is user_main_page line 70')
        ftp_menu = {
            'show':self.show_files,
            'put':self.put,
            'get':self.get_file,
            'cd':self.cd,
            'exits':self.exits
        }
        if user_input in ftp_menu:
            # print('line 69')
            ftp_menu[user_input]()
            # self.get_file()
        else:
            print('您选择的不在我提供的服务范围！client_startup.py file in line 70')
            # return Ftp_Client_Start.start(self)
            return None

    def show_files(self):
        print('show def')
        f_client_conn.send(b'show_files')
        result = f_client_conn.recv(204800)
        # print(result)
        file_dict = dict(eval(result.decode('utf-8')))
        # print(file_dict)
        print('返回上层目录：..')
        for element_key in file_dict:
            print(file_dict[element_key],'：',element_key)

    def put(self):
        #pass
        print('put file')
        print('this is ftp client line 72')
        f_client_conn.send('put_file'.encode('utf-8'))  # 发送下载文件请求，用于测试服务器下载功能是否正常
        put_file_name = input('请输入您需要上传的文件的绝对路径：')
        print('您要上传的文件为：',put_file_name)
        if os.path.exists(put_file_name):
            f_client_conn.send(put_file_name.encode('utf-8'))
            f_size = os.path.getsize(put_file_name)  # 文件大小
            print('被请求上传文件的大小', f_size)
            f_client_conn.send(str(f_size).encode('utf-8'))  # 发送文件大小
            put_break = f_client_conn.recv(204800).decode('utf-8') # 接收到put_break表示服务器文件存在
            print('put_break:', put_break)
            if put_break == 'put_break':
                print('服务器端出错')
                return None
            put_size = 0  # 已发送文件大小
            # conn.send('abcdefg'.encode('utf-8'))
            i = 0
            with open(put_file_name, 'rb') as f:
                while f_size - put_size >= 204800:
                    print('文件大小：', f_size)
                    # print('未发送文件大小：', f_size - sended_size)
                    # print('读取前光标句柄所在位置：', f.tell())
                    if f_size - put_size > 204800:
                        contest = f.read(204800)
                    else:
                        contest = f.read(f_size - put_size)
                    # print('将要发送的内容大小：', len(contest))
                    f_client_conn.send(contest)  # 发送本次读取到的信息
                    put_size += len(contest)
                    f.seek(put_size)  # 将光标句柄移至已发送的位置（即从光标开始往后都是未发送的内容)
                    # print('光标句柄所在位置：', f.tell())
                    i += 1
                    print('发送了:', i, '次')
                    print('已发送文件大小：', put_size)
                else:
                    print('准备发送最后一次')
                    print('读取前光标句柄所在位置：', f.tell())
                    print('剩余文件大小', f_size - put_size)
                    contest = f.read(f_size - put_size)
                    print('contest len:', len(contest))
                    f_client_conn.sendall(contest)
                    # conn.send(b'send_session')
                    print('文件发送完毕！')
                    # conn.send(b'send_session')
                    # return self.start()
        else:
            print('您要上传的文件不存在，请查询后再操作！')
            f_client_conn.send('client_file_error'.encode('utf-8'))
            return None

    ######  从服务器上下载文件
    def get_file(self):
        print('get file')
        f_client_conn.send('get_file'.encode('utf-8'))  # 发送下载文件请求，用于测试服务器下载功能是否正常
        f_name = input('请输入您需要下载的文件名称：')
        f_client_conn.send(f_name.encode('utf-8')) # 发送下载文件名称
        f_data = f_client_conn.recv(204800)
        print(f_data)
        print('line 92',f_data)
        if os.path.exists(user_home+'/'+f_name):
            print('该文件已存在！')
            f_client_conn.send('send_break'.encode('utf-8'))
            return None
        elif f_data == 'file_error':
            print('服务器文件故障或文件不存在，请联系管理员！')
            return None
        elif f_data.decode('utf-8').isdigit():# 服务器存在文件且将文件大小传输过来（表示本地不存在此文件）
            # f_client_conn.send(bytes('get_file', f_name))
            load_file_size = int(f_data.decode('utf-8')) # 将要下载的文件大小
            print('文件大小%s'%load_file_size)
            f_client_conn.send(b'start download file')
            print('start download ftp file')
            f_size = 0  # 已接收文件的大小
            while load_file_size - f_size > 0:   # 大于小表示文件未传输完毕
                data = f_client_conn.recv(204800)   # 服务传输过来的文件块数据
                with open(user_home+'/'+f_name, 'ab+') as f:
                    f.write(data)
                    f.flush()
                    f_size += len(data)
                    print('已接收：', f_size)
            else:print('文件接收完毕')
        else:
            print('文件传输异常，请联系服务器管理人员！')
            f_client_conn.send(b'send_break')
            return None

    # 目录切换
    def cd(self):
        # user_home
        print('changed folder line in 165')
        self.show_files()
        change_folder= input('请输入您需要切换的目录：')
        f_client_conn.send('cd_files'.encode('utf-8'))
        f_client_conn.send(change_folder.encode('utf-8'))
        return self.show_files()

    def exits(self):
        f_client_conn.send(b'exits')
        print('欢迎您再次使用Aling_FTP，再见！')
        exit()

Ftp_Client_Start()
f_client_conn.close()
# -*- coding:utf-8 -*-
#  Author:aling
# 客户端
import socket,os


f_client_conn = socket.socket()
h = '127.0.0.1'   #服务器端IP
p = 8823
f_client_conn.connect((h, p))


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
        # print('this is client_startup.py')
        self.start()

    def start(self):
        ftp_menu = '''
            show：显示当前文件夹下的所有文件及文件详细信息
            put：上传文件
            get：下载文件
            cd：目录切换
        '''
        while True:
            print(ftp_menu)
            user_input = input('请输入需要的操作：')
            # print(self)
            self.user_main_page(user_input)

    def user_main_page(self,user_input):
        # print('this is user_main_page')
        # print(self)
        ftp_menu = {
            'show':self.show,
            'put':self.put,
            'get':self.get_file,
            'cd':self.cd
        }
        if user_input in ftp_menu:
            print('line 69')
            ftp_menu[user_input]()
            # self.get_file()
        else:
            print('您选择的不在我提供的服务范围！client_startup.py file in line 70')
            # return Ftp_Client_Start.start(self)
            return None

    def show(self):
        #pass
        print('show list')

    def put(self):
        #pass
        print('put file')

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
            # else:   # 接收剩余的文件数据
            #     data = f_client_conn.recv(load_file_size - f_size)
            #     print('剩余文件大小%s'%len(data))
            #     with open(user_home+'/'+f_name, 'ab+') as f:
            #         f.write(data)
            #         f.flush()
            #         f_size += len(data)
            #         print('已接收2：', f_size)
            #         print('文件接收完毕')
        else:
            print('文件传输异常，请联系服务器管理人员！')
            f_client_conn.send(b'send_break')
            return None

    def cd(self):
        # pass
        print('changed folder')

Ftp_Client_Start()


f_client_conn.close()
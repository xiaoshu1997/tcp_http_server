#1. 创建tcp客户端套接字
#2. 和服务器建立链接
#3. 发送数据到服务器端
#4. 接收服务器的数据
#5. 关闭套接字

import socket
import time

if __name__ == '__main__':
    #1. 创建tcp客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    #2. 和服务器建立链接
    client_socket.connect( ("192.168.0.103", 9090) )


    #3. 发送数据到服务器端
    client_socket.send("Hello 你好啊".encode("utf-8"))

    # 4. 接收服务器的数据
    k =  client_socket.recv(1024)
    print(k.decode("utf-8"))


   # time.sleep(10000)

    #5. 关闭套接字
    client_socket.close()
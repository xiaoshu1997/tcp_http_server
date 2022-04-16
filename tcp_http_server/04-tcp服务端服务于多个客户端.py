# URL组成部分

# 1. 协议部分 http ftp
# 2. 域名部分 baidu.com
# 3. 资源路径部分
# 4. 参数  ？page=1&count=10


import socket, threading

#   但是要顺序服务

# 处理接收客户端
def handler_client_request(sc, addr_port):
    # 这里让子线程来专门负责 客户端的消息
    print("addr_port -> ", addr_port)
    # 5. 接收数据

    while True:

       data = sc.recv(1024)

       if data:
         data = data.decode("utf-8")
         print("接收到的数据有 -> ", data, addr_port)

         # 6. 发送数据
         sc.send(data.upper().encode("utf-8"))
       else:
           print("客户端下线ing")
           break

    # 7. 关闭套接字
    sc.close()


if __name__ == '__main__':



    #1. 创建服务器端套接字对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   # 当前套接字   端口号复用的选项  1 可以复用端口
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #2. 绑定端口号
    server_socket.bind(  ("", 9090) )

    #3. 设置监听
    server_socket.listen(5)

    #4. 等待接收客户端的链接请求 addr_port是主机自动给客户端分配的 端口
    # 这里会阻塞，等待客户端来

    while True:

        sc, addr_port = server_socket.accept()

        sub_thread = threading.Thread(target=handler_client_request, args=(sc, addr_port))

        # 设置守护主线程，主线程退出，子线程销毁
        sub_thread.setDaemon(True)

        sub_thread.start()





    server_socket.close()
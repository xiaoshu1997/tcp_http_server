import socket




if __name__ == '__main__':



    #1. 创建服务器端套接字对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2. 绑定端口号
    server_socket.bind(  ("", 9090) )

    #3. 设置监听
    # listen后的套接字， 智能等待客户端连接，不能用于接消息 和  发消息
    server_socket.listen(5)

    #4. 等待接收客户端的链接请求 addr_port是主机自动给客户端分配的 端口
    # 这里会阻塞，等待客户端来
    sc, addr_port = server_socket.accept()
    print("addr_port -> ", addr_port)
    #5. 接收数据


    data = sc.recv(1024)
    data = data.decode("utf-8")
    print("接收到的数据有 -> ",data)

    #6. 发送数据
    sc.send( data.upper().encode("utf-8") )

    #7. 关闭套接字
    sc.close()
    server_socket.close()
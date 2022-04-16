import socket

# 判断是否为主模块代码

if __name__ == '__main__':

    # 创建tcp服务端套接字
    tcp_sercer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sercer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定点口号
    tcp_sercer_socket.bind( ("", 8000) )

    # 设置监听
    tcp_sercer_socket.listen(128)

    # 循环等待接收客户端的链接请求
    while True:
        # 等待接收客户端连接请求
        new_socket, ip_port = tcp_sercer_socket.accept()

        # 接收客户端的请求信息
        recv_data = new_socket.recv(4096)

        print(recv_data)

        # 打开文件读取 文件数据

        with open("index.html", "r") as f:  # f表示打开的文件对象
           file_data = f.read()

       # 把数据封装称为http 响应的报文数据 -- 响应行，响应头 空行 响应体

        # 响应行
        responsr_line = "HTTP?/1.1 200 OK\r\n"

        #响应头
        response_header = "Server: PWS/1.0\r\n"

        #响应体
        response_body = file_data


        response_data = responsr_line + response_header + "\r\n" + response_body


        # 发送
        new_socket.send(response_data.encode("utf-8"))  # 这里要注意我们只能识别二进制文件

        # 关闭客户端套接字
        new_socket.close()









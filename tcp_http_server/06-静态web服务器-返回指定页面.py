import socket

# 判断是否为主模块代码

def main():

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

        if len(recv_data) == 0:
            new_socket.close()
            return


        print(recv_data)

        # 对二进制数据解码
        recv_content = recv_data.decode("utf-8")
        print(recv_content)

        # 对数据按照空格分割
        request_list = recv_content.split(" ", maxsplit=2)
        request_path = request_list[1]
        print("资源路径：", request_path)
        request_path = request_path[1:]


        if request_path == "":
            request_path = "index.html"


        #os.path.exits(request_path)




        try:

            # 打开文件读取 文件数据
            with open(request_path, "rb") as f:  # f表示打开的文件对象
               file_data = f.read()

        except Exception as e:
            # 代码执行到这里 说明找不到文件 返回404

            # 响应行
            responsr_line = "HTTP?/1.1 404 Not Found\r\n"

            #响应头
            response_header = "Server: PWS/1.0\r\n"

            # 读取404页面数据
            with open("error.html", "rb") as f:
                file_data = f.read()


            #响应体
            response_body = file_data


            response_data = (responsr_line + response_header + "\r\n").encode("utf-8") + response_body

            # 发送
            new_socket.send(response_data)  # 这里要注意我们只能识别二进制文件


            pass
        else:  # 说明访问文件存在

           # 把数据封装称为http 响应的报文数据 -- 响应行，响应头 空行 响应体

            # 响应行
            responsr_line = "HTTP?/1.1 200 OK\r\n"

            #响应头
            response_header = "Server: PWS/1.0\r\n"

            #响应体
            response_body = file_data


            response_data = (responsr_line + response_header + "\r\n").encode("utf-8") + response_body


            # 发送
            new_socket.send(response_data)  # 这里要注意我们只能识别二进制文件

        finally:
            # 关闭客户端套接字
            new_socket.close()

if __name__ == '__main__':

    main()









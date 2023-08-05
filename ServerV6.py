import socket

def main():
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_socket.bind(("::", 12345))  # 使用IPv6任意地址和端口
    server_socket.listen(2)  # 最多监听两个客户端
    print("Server started, waiting for connections...")

    clients = []  # 存储已连接的客户端信息

    while len(clients) < 2:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to: {client_address}")
        clients.append((client_socket, client_address))

    # 向A发送B的地址和端口号
    clients[0][0].sendall(f"{clients[1][1][0]} {clients[1][1][1]}".encode("utf-8"))
    # 向B发送A的地址和端口号
    clients[1][0].sendall(f"{clients[0][1][0]} {clients[0][1][1]}".encode("utf-8"))

    for client_socket, _ in clients:
        client_socket.close()

if __name__ == "__main__":
    main()

import socket

def get_own_ipv6_address():
    # 获取本地IPv6地址
    ipv6_address = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
    return ipv6_address

def main():
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_socket.bind(("::", 12345))  # 使用IPv6任意地址和端口
    server_socket.listen(1)
    print("Server started, waiting for connections...")

    client_socket, client_address = server_socket.accept()
    print(f"Connected to: {client_address}")

    while True:
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        print(f"Received from client: {data}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    print(f"Your IPv6 Address: {get_own_ipv6_address()}")
    main()

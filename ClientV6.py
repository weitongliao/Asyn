import socket


def main():
    server_ipv6_address = input("Enter the server's IPv6 address: ")

    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client_socket.connect((server_ipv6_address, 12345))
    print("Connected to server")

    peer_info = client_socket.recv(1024).decode("utf-8").split()  # 接收对方的地址和端口号
    peer_ipv6_address = peer_info[0]
    peer_port = int(peer_info[1])

    peer_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    peer_socket.connect((peer_ipv6_address, peer_port))
    print("Connected to peer")

    while True:
        message = input("Enter your message (or 'exit' to quit): ")
        peer_socket.send(message.encode("utf-8"))

        if message == "exit":
            break

    peer_socket.close()
    client_socket.close()


if __name__ == "__main__":
    main()

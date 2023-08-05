import socket

def assign_client_id(client_socket, client_address):
    # 分配唯一的ID给客户端，这里简单使用客户端的IP和端口号作为ID
    return f"{client_socket}:{client_address}"

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5)
    print("Server started, listening on port 12345")

    clients = {}  # 存储客户端的ID和字符串数据

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")

        client_id = assign_client_id(client_socket, client_address)
        clients[client_id] = ""  # 初始化空字符串用于存储客户端的数据

        data = client_socket.recv(1024).decode("utf-8")
        clients[client_id] = data

        print("id", client_id)

        print(f"Received data from {client_id}: {data}")

        client_socket.send(f"Your ID is {client_id}".encode("utf-8"))
        client_socket.close()

if __name__ == "__main__":
    main()



# import asyncio
# import websockets
#
# connected_clients = set()
#
# async def handle_client(websocket, path):
#     # 接收客户端的标识符
#     client_id = await websocket.recv()
#     print(f"Client {client_id} connected.")
#
#     connected_clients.add(websocket)
#
#     try:
#         async for message in websocket:
#             # 收到消息后，将消息转发给其他所有客户端
#             for client in connected_clients:
#                 if client != websocket:
#                     await client.send(message)
#     except websockets.exceptions.ConnectionClosed:
#         pass
#     finally:
#         connected_clients.remove(websocket)
#
# async def main():
#     server = await websockets.serve(handle_client, "0.0.0.0", 12345) # 35.215.165.210
#     print("Signaling server started at ws://0.0.0.0:12345")
#     await server.wait_closed()
#
# # if __name__ == "__main__":
# #     asyncio.run(main())
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()

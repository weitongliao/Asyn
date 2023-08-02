import asyncio
import websockets

connected_clients = set()

async def handle_client(websocket, path):
    # 接收客户端的标识符
    client_id = await websocket.recv()
    print(f"Client {client_id} connected.")

    connected_clients.add(websocket)

    try:
        async for message in websocket:
            # 收到消息后，将消息转发给其他所有客户端
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, "0.0.0.0", 12345) # 35.215.165.210
    print("Signaling server started at ws://0.0.0.0:12345")
    await server.wait_closed()

# if __name__ == "__main__":
#     asyncio.run(main())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

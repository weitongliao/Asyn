import asyncio
import websockets

async def send_sdp_to_server():
    uri = "ws://35.215.165.210:12345"
    async with websockets.connect(uri) as websocket:
        client_id = "client_a"
        await websocket.send(client_id)

        # 假设客户端 A 有一个本地的 SDP
        local_sdp = "..."  # 从本地获取 SDP
        print(f"Sending SDP to Signaling Server: {local_sdp}")
        await websocket.send(local_sdp)

        # 等待接收来自客户端 B 的 SDP
        remote_sdp = await websocket.recv()
        print(f"Received SDP from Signaling Server: {remote_sdp}")

        # 在这里，客户端 A 和客户端 B 均具有了对方的 SDP，可以使用 asyncio 建立 P2P 连接
        # 在实际应用中，需要使用具体的 WebRTC 库，例如 aiortc，来完成 P2P 连接的建立和数据交换

loop = asyncio.get_event_loop()
loop.run_until_complete(send_sdp_to_server())
loop.close()

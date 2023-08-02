import asyncio
import json
import websockets
from aiortc import RTCPeerConnection, RTCSessionDescription, RTCIceCandidate

async def connect_to_server():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        client_id = "client_b"
        await websocket.send(client_id)

        # 创建 PeerConnection 对象
        pc = RTCPeerConnection()

        # 添加本地音频或视频媒体流（这里添加一个本地音频轨道，需要根据实际需求设置）
        audio_track = ...  # 获取本地音频轨道
        pc.addTrack(audio_track)

        # 等待接收来自客户端 A 的 SDP
        message = await websocket.recv()
        data = json.loads(message)
        remote_sdp = RTCSessionDescription(sdp=data["sdp"], type="offer")
        await pc.setRemoteDescription(remote_sdp)

        # 创建一个本地 SDP
        local_sdp = await pc.createAnswer()
        await pc.setLocalDescription(local_sdp)

        # 发送本地 SDP 到信令服务器
        await websocket.send(json.dumps({"sdp": pc.localDescription.sdp}))

        # 等待接收来自客户端 A 的 ICE 候选者，并添加到 PeerConnection 中
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            if "ice" in data:
                ice_candidate = RTCIceCandidate(sdpMid=data["sdpMid"], sdpMLineIndex=data["sdpMLineIndex"], candidate=data["candidate"])
                await pc.addIceCandidate(ice_candidate)

if __name__ == "__main__":
    asyncio.run(connect_to_server())

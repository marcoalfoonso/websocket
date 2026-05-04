import cv2
import asyncio
import websockets

async def send_video():
    uri = "wss://threed-model-yvro.onrender.com"
    async with websockets.connect(uri) as websocket:

        cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            _, buffer = cv2.imencode('.jpg', frame)
            await websocket.send(buffer.tobytes())

asyncio.run(send_video())
import asyncio
import os
import websockets

PORT = int(os.environ.get("PORT", 10000))

clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            #retransmitir a todos
            for client in clients:
                if client != websocket:
                    await client.send(message)
    finally:
        clients.remove(websocket)


async def main():
    async with websockets.serve(handler,"0.0.0.0",PORT):
        print(f"Servidor WebSocket iniciado en el puerto {PORT}")
        await asyncio.Future()  # Mantener el servidor en ejecución

if __name__ == "__main__":
    asyncio.run(main())

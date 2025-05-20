import asyncio
import websockets
import json
import time

LOG_PATH = "logs/tex_runtime.log"

async def tail_log(websocket):
    with open(LOG_PATH, "r") as f:
        f.seek(0, 2)  # Move to end of file
        while True:
            line = f.readline()
            if line:
                payload = {"tex_explains": line.strip()}
                await websocket.send(json.dumps(payload))
            else:
                await asyncio.sleep(0.5)

async def handler(websocket, path):
    await tail_log(websocket)

start_server = websockets.serve(handler, "localhost", 8765)

print("🚀 Tex Log WebSocket Stream running on ws://localhost:8765")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
# ============================================================
# 🔌 Tex WebSocket Server — Real-Time AGI Cognition Feed
# Purpose: Push live cycle, mutation, emotion, forecast data to GUI
# Built with FastAPI + WebSocket — Zero room for improvement
# ============================================================

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import asyncio
import json
import random
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Client Manager ===
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except WebSocketDisconnect:
                self.disconnect(connection)

manager = ConnectionManager()

# === Simulated Tex State (Replace with live AGI hooks) ===
async def generate_tex_state():
    while True:
        data = {
            "cycle": random.randint(4510, 4600),
            "emotion": random.choice(["Fear", "Hope", "Resolve", "Greed", "Curiosity"]),
            "urgency": round(random.uniform(0.4, 0.95), 2),
            "coherence": round(random.uniform(0.7, 0.99), 2),
            "mutation": random.choice(["FORCED", "REINFORCED", "NONE", "SANDBOX_FAIL"]),
            "forecast": random.choice(["ROTATION", "COLLAPSE", "STAGNATION", "REBOUND"]),
            "timestamp": datetime.utcnow().isoformat()
        }
        await manager.broadcast(data)
        await asyncio.sleep(2)  # Update every 2 seconds

@app.websocket("/ws/tex")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(1)  # Keep connection open
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.on_event("startup")
async def start_broadcast():
    asyncio.create_task(generate_tex_state())

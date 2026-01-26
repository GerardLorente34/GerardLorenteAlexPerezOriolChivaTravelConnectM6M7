from typing import Dict, List
from fastapi import WebSocket
import json


class ConnectionManager:
    def __init__(self):
        # Diccionario: viaje_id -> lista de WebSockets conectados
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, viaje_id: int):
        await websocket.accept()
        if viaje_id not in self.active_connections:
            self.active_connections[viaje_id] = []
        self.active_connections[viaje_id].append(websocket)

    def disconnect(self, websocket: WebSocket, viaje_id: int):
        if viaje_id in self.active_connections:
            self.active_connections[viaje_id].remove(websocket)
            if not self.active_connections[viaje_id]:
                del self.active_connections[viaje_id]

    async def broadcast(self, viaje_id: int, message: dict):
        if viaje_id in self.active_connections:
            disconnected = []
            for connection in self.active_connections[viaje_id]:
                try:
                    await connection.send_json(message)
                except Exception:
                    disconnected.append(connection)
            
            # Eliminar conexiones fallidas
            for conn in disconnected:
                self.disconnect(conn, viaje_id)


manager = ConnectionManager()
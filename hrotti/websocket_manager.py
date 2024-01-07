import json

from fastapi import WebSocket

from .methods import BlockInfo, handle_request, RPCRequest


async def accept_ws_request(info: BlockInfo, websocket: WebSocket):
    data = await websocket.receive_json()
    try:
        request = RPCRequest(**data)
        await websocket.send_json(handle_request(info, request))
    except json.JSONDecodeError:
        await websocket.send_text("Error: Invalid JSON")

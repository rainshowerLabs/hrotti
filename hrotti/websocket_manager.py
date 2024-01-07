import json

from fastapi import WebSocket

from .methods import BlockInfo, handle_request


async def accept_ws_request(info: BlockInfo, websocket: WebSocket):
    data = await websocket.receive_text()
    try:
        request = json.loads(data)
        await websocket.send_text(handle_request(request.get("method"), info))
    except json.JSONDecodeError:
        await websocket.send_text("Error: Invalid JSON")

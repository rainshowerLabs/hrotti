import json

from fastapi import WebSocket

from .methods import BlockInfo, handle_request, RPCRequest


async def accept_ws_request(info: BlockInfo, websocket: WebSocket):
    data = await websocket.receive_json()
    try:
        request = RPCRequest(**data)
        response_dict = handle_request(info, request)
        await websocket.send_text(json.dumps(response_dict))
    except json.JSONDecodeError:
        await websocket.send_text("Error: Invalid JSON")

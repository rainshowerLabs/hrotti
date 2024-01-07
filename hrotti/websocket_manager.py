import json

from fastapi import WebSocket

from .methods import BlockInfo, RPCRequest, handle_request


# Fakes subscription, sends dummy data every n seconds
def fake_subscribe(websocket: WebSocket):
    pass


# Proceses WS connection
#
# If we do not receive a subscription process it as a regular request,
# otherwise fake a subscription
async def accept_ws_request(info: BlockInfo, websocket: WebSocket):
    data = await websocket.receive_json()
    try:
        request = RPCRequest(**data)
        await websocket.send_json(handle_request(info, request))
    except json.JSONDecodeError:
        await websocket.send_text("Error: Invalid JSON")

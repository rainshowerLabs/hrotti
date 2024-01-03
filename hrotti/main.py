import json

from fastapi import FastAPI, WebSocket

from .methods import RPCRequest, block_info, handle_request

app = FastAPI()

info = block_info(
    head="0x5BAD55",
    chain_id="0x1",
    coinbase="0x407d73d8a49eeb85d32cf465507dd71d507100c1",
    gasprice="0x1",
    balance="0x1",
)


@app.post("/http")
async def handle_json_rpc(request: RPCRequest):
    return handle_request(request, info)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        try:
            request = json.loads(data)
            await websocket.send_text(handle_request(request.get("method"), info))
        except json.JSONDecodeError:
            await websocket.send_text("Error: Invalid JSON")

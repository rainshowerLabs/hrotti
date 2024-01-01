import json

from fastapi import FastAPI, WebSocket

from .methods import RPCRequest, handle_request

app = FastAPI()


@app.post("/http")
async def handle_json_rpc(request: RPCRequest):
    return handle_request(request)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        try:
            request = json.loads(data)
            if request.get("method") == "eth_blockNumber":
                response = json.dumps(
                    {"jsonrpc": "2.0", "id": request.get("id"), "result": "0x5BAD55"}
                )
                await websocket.send_text(response)
        except json.JSONDecodeError:
            await websocket.send_text("Error: Invalid JSON")

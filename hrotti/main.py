from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
import json

app = FastAPI()

class RPCRequest(BaseModel):
    jsonrpc: str
    method: str
    params: list
    id: int

@app.post("/jsonrpc")
async def handle_json_rpc(request: RPCRequest):
    if request.method == "eth_blockNumber":
        # Mock response for demonstration
        return {"jsonrpc": "2.0", "id": request.id, "result": "0x5BAD55"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        try:
            request = json.loads(data)
            if request.get("method") == "eth_blockNumber":
                response = json.dumps({"jsonrpc": "2.0", "id": request.get("id"), "result": "0x5BAD55"})
                await websocket.send_text(response)
        except json.JSONDecodeError:
            await websocket.send_text("Error: Invalid JSON")

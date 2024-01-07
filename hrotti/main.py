import json

from fastapi import FastAPI, WebSocket

from .methods import BlockInfo, RPCRequest, handle_request
from .websocket_manager import accept_ws_request

app = FastAPI()

# Basic info about the block we're faking
#
# TODO:
# replace this with a json or something of a real block dump
# the goal is to be able to just dump blocks and fakecall them by index and everything
info = BlockInfo(
    head="0x5BAD55",
    chain_id="0x1",
    coinbase="0x407d73d8a49eeb85d32cf465507dd71d507100c1",
    gasprice="0x1",
    balance="0x1",
)


@app.post("/http")
async def handle_json_rpc(request: RPCRequest):
    return handle_request(info, request)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await accept_ws_request(info, websocket)

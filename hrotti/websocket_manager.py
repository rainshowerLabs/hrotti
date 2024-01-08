import asyncio
import json
import random

from fastapi import WebSocket

from .methods import BlockInfo, RPCRequest, handle_request

sub_confirmation = {"id": 0, "result": "", "jsonrpc": "2.0"}

fake_new_head = {
    "jsonrpc": "2.0",
    "method": "eth_subscription",
    "params": {
        "subscription": "",
        "result": {
            "parentHash": "0x00bdd9454ead08e03ad9d1516cdddc7db529de716bf8311a96fc1a2a27889377",
            "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
            "miner": "0x388c818ca8b9251b393131c08a736a67ccb19297",
            "stateRoot": "0xe920ed2fb25543c04e537a6487e5a99c7b9e6516cb36be22c7130d99ba9702ca",
            "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
            "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
            "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "difficulty": "0x0",
            "number": "0x0",
            "gasLimit": "0x1c9c380",
            "gasUsed": "0x0",
            "timestamp": "0x659b269b",
            "extraData": "0xd883010d05846765746888676f312e32312e34856c696e7578",
            "mixHash": "0x64b6af940d7c2107a0c9d46462fb777cf444da64b055ba6d594568eb50dd9339",
            "nonce": "0x0000000000000000",
            "baseFeePerGas": "0x8d7a7855a",
            "withdrawalsRoot": "0x1b4925152dfdbbb40ca2140d1d2f42a2d505b9e8e9dea2f028463c097141b9ef",
            "blobGasUsed": "",
            "excessBlobGas": "",
            "parentBeaconBlockRoot": "",
            "hash": "0x38484f6cd1a4b8b471e25f3ad52a562a15f8c95cfcaa8cd97d41ca587f69e1ad",
        },
    },
}


# Fakes subscription, sends dummy data every n seconds
async def fake_subscribe(sub_request: RPCRequest, websocket: WebSocket):
    local_conf = sub_confirmation
    local_conf["id"] = sub_request.id

    # generate a random number with a int16 max and convert do hex for sub id
    sub_id = hex(random.randint(0, 32767))
    local_conf["result"] = sub_id

    # send confirmation and prep our client to listen for subscriptions
    await websocket.send_json(local_conf)

    local_fake_head = fake_new_head
    local_fake_head["params"]["subscription"] = sub_id

    # we now want to send a new head block every 6 seconds with an incrementing block number
    block_num = -1
    while True:
        block_num = block_num + 1
        local_fake_head["params"]["result"]["number"] = hex(block_num)
        await websocket.send_json(local_fake_head)
        await asyncio.sleep(6)


# Proceses WS connection
#
# If we do not receive a subscription process it as a regular request,
# otherwise fake a subscription
async def accept_ws_request(info: BlockInfo, websocket: WebSocket):
    data = await websocket.receive_json()
    try:
        request = RPCRequest(**data)

        # check if we're receiving a subscription request
        if request.method == "eth_subscribe":
            await fake_subscribe(request, websocket)
        else:
            await websocket.send_json(handle_request(info, request))
    except json.JSONDecodeError:
        await websocket.send_text("Error: Invalid JSON")

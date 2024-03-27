from typing import Any, List, Optional

from pydantic import BaseModel


class RPCRequest(BaseModel):
    jsonrpc: str
    method: str
    params: Optional[List[Any]] = None
    id: int


class BlockInfo(BaseModel):
    head: str
    chain_id: str
    coinbase: str
    gasprice: str
    balance: str


def return_block(head, transaction):
    return {
        "difficulty": "0x4ea3f27bc",
        "extraData": "0x476574682f4c5649562f76312e302e302f6c696e75782f676f312e342e32",
        "gasLimit": "0x1388",
        "gasUsed": "0x0",
        "hash": "0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae",
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "miner": "0xbb7b8287f3f0a933474a79eae42cbca977791171",
        "mixHash": "0x4fffe9ae21f1c9e15207b1f472d5bbdd68c9595d461666602f2be20daf5e7843",
        "nonce": "0x689056015818adbe",
        "number": head,
        "parentHash": "0xe99e022112df268087ea7eafaf4790497fd21dbeeb6bd7a1721df161a6657a54",
        "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0x220",
        "stateRoot": "0xddc8b0234c2e0cad087c8b389aa7ef01f7d79b2570bccb77ce48648aa61c904d",
        "timestamp": "0x55ba467c",
        "totalDifficulty": "0x78ed983323d",
        "transactions": [transaction],
        "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "uncles": ["0x1"],
    }


logs = {
    "logIndex": "0x1",
    "blockNumber": "0x1b4",
    "blockHash": "0x8216c5785ac562ff41e2dcfdf5785ac562ff41e2dcfdf829c5a142f1fccd7d",
    "transactionHash": "0xdf829c5a142f1fccd7d8216c5785ac562ff41e2dcfdf5785ac562ff41e2dcf",
    "transactionIndex": "0x0",
    "address": "0x16c5785ac562ff41e2dcfdf829c5a142f1fccd7d",
    "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "topics": ["0x59ebeb90bc63057b6515673c3ecf9438e5058bca0f92585014eced636878c9a5"],
}

transaction = {
    "blockHash": "0x1d59ff54b1eb26b013ce3cb5fc9dab3705b415a67127a003c3e61eb445bb8df2",
    "blockNumber": "0x5daf3b",
    "from": "0xa7d9ddbe1f17865597fbd27ec712455208b6b76d",
    "gas": "0xc350",
    "gasPrice": "0x4a817c800",
    "hash": "0x88df016429689c079f3b2f6ad39fa052532c56795b733da78a91ebe6a713944b",
    "input": "0x68656c6c6f21",
    "nonce": "0x15",
    "to": "0xf02c1c8e6114b1dbe8937a39260b5b0a374432bb",
    "transactionIndex": "0x41",
    "value": "0xf3dbb76162000",
    "v": "0x25",
    "r": "0x1b5e176d927f8e9ab405058b2d2457392da3e20f328b16ddabcebc33eaac5fea",
    "s": "0x4ba69724e8f69de52f0125ad8b3c5c2cef33019bac3249e2c0a2192766d1721c",
}


# Return response based off of requested method
# TODO: replace hardcoded block values with the thing mentioned in main.py TODO
def handle_request(info: BlockInfo, request: RPCRequest):
    print(request)
    try:
        match request.method:
            case "eth_blockNumber":
                return {"jsonrpc": "2.0", "id": request.id, "result": info.head}
            case "eth_accounts":
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "result": ["0x407d73d8a49eeb85d32cf465507dd71d507100c1"],
                }
            case "eth_call":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x0"}
            case "eth_chainId":
                return {"jsonrpc": "2.0", "id": request.id, "result": info.chain_id}
            case "eth_coinbase":
                return {"jsonrpc": "2.0", "id": request.id, "result": info.coinbase}
            case "eth_estimateGas":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0xffff"}
            case "eth_gasPrice":
                return {"jsonrpc": "2.0", "id": request.id, "result": info.gasprice}
            case "eth_getBalance":
                return {"jsonrpc": "2.0", "id": request.id, "result": info.balance}
            case "eth_getBlockByHash":
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "result": return_block(info.head, transaction),
                }
            case "eth_getBlockByNumber":
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "result": return_block(info.head, transaction),
                }
            case "eth_getBlockTransactionCountByHash":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x1"}
            case "eth_getBlockTransactionCountByNumber":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x1"}
            case "eth_getCode":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0xff"}
            case "eth_getLogs":
                return {"jsonrpc": "2.0", "id": request.id, "result": [logs]}
            case "eth_getFilterChanges":
                return {"jsonrpc": "2.0", "id": request.id, "result": [logs]}
            case "eth_getFilterLogs":
                return {"jsonrpc": "2.0", "id": request.id, "result": [logs]}
            case "eth_getStorageAt":
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "result": "0x00000000000000000000000000000000000000000000000000000000000004d2",
                }
            case "eth_getTransactionByBlockHashAndIndex":
                return {"jsonrpc": "2.0", "id": request.id, "result": transaction}
            case "eth_getTransactionByBlockNumberAndIndex":
                return {"jsonrpc": "2.0", "id": request.id, "result": transaction}
            case "eth_getTransactionByHash":
                return {"jsonrpc": "2.0", "id": request.id, "result": transaction}
            case "eth_getTransactionCount":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x1"}
            case "eth_getTransactionReceipt":
                return {"jsonrpc": "2.0", "id": request.id, "result": transaction}
            case "eth_getUncleByBlockHashAndIndex":
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "result": return_block(info.head, transaction),
                }
            case "eth_getUncleByBlockNumberAndIndex":
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "result": return_block(info.head, transaction),
                }
            case "eth_getUncleCountByBlockHash":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x0"}
            case "eth_getUncleCountByBlockNumber":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x0"}
            case "eth_newBlockFilter":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x1"}
            case "eth_newFilter":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x1"}
            case "eth_newPendingTransactionFilter":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x1"}
            case "eth_sendRawTransaction":
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "result": "0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331",
                }
            case "eth_sendTransaction":
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "result": "0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331",
                }
            case "eth_syncing":
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "result": {
                        "currentBlock": info.head,
                        "healedBytecodeBytes": "0x0",
                        "healedBytecodes": "0x0",
                        "healedTrienodes": "0x0",
                        "healingBytecode": "0x0",
                        "healingTrienodes": "0x0",
                        "highestBlock": info.head,
                        "startingBlock": "0x3cbed5",
                        "syncedAccountBytes": "0x0",
                        "syncedAccounts": "0x0",
                        "syncedBytecodeBytes": "0x0",
                        "syncedBytecodes": "0x0",
                        "syncedStorage": "0x0",
                        "syncedStorageBytes": "0x0",
                    },
                }
            case _:
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "error": "Method does not exist!",
                }
    except Exception as e:
        return {"jsonrpc": "2.0", "id": request.id, "error": str(e)}

from typing import Any, List

from pydantic import BaseModel


class RPCRequest(BaseModel):
    jsonrpc: str
    method: str
    params: List[Any]
    id: int


def handle_request(request: RPCRequest):
    try:
        match request.method:
            case "eth_blockNumber":
                return {"jsonrpc": "2.0", "id": request.id, "result": "0x5BAD55"}
            case _:
                return {
                    "jsonrpc": "2.0",
                    "id": request.id,
                    "error": "Method does not exist!",
                }
    except Exception as e:
        return {"jsonrpc": "2.0", "id": request.id, "error": str(e)}

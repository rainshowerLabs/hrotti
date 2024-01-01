from pydantic import BaseModel


class RPCRequest(BaseModel):
    jsonrpc: str
    method: str
    params: list
    id: int


def handle_request(request: RPCRequest):
    pass

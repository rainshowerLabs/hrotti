import pytest
from hrotti.methods import handle_request, RPCRequest, BlockInfo

test_block_info = BlockInfo(
    head="0x1", chain_id="0x4", coinbase="0x123", gasprice="0x5208", balance="0x0"
)


# Define a fixture for RPCRequest
@pytest.fixture
def rpc_request():
    return RPCRequest(jsonrpc="2.0", id=1, method="", params=[])


# Test for eth_blockNumber
def test_handle_request_eth_blockNumber(rpc_request):
    rpc_request.method = "eth_blockNumber"
    response = handle_request(test_block_info, rpc_request)
    assert response == {"jsonrpc": "2.0", "id": 1, "result": test_block_info.head}


# Test for eth_accounts
def test_handle_request_eth_accounts(rpc_request):
    rpc_request.method = "eth_accounts"
    response = handle_request(test_block_info, rpc_request)
    assert response == {
        "jsonrpc": "2.0",
        "id": 1,
        "result": ["0x407d73d8a49eeb85d32cf465507dd71d507100c1"],
    }


# Test for a method that doesn't exist
def test_method_not_exist():
    request = RPCRequest(jsonrpc="2.0", method="non_existent_method", params=[], id=1)
    expected_response = {"jsonrpc": "2.0", "id": 1, "error": "Method does not exist!"}
    assert handle_request(test_block_info, request) == expected_response

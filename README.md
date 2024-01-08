![hrotti](https://github.com/makemake-kbo/hrotti/assets/55022497/faba2145-7a4d-4973-a3b7-a25341700a16)
# Hrotti

Hrotti is a tool for simulating fake Ethereum JSON-RPC responses, with support for both HTTP and WS (including subscriptions).   

If you're developing software that interacts with the Ethereum JSON-RPC API, its hard to get consistant results which makes it harder to test and debug your code. Hrotti solves this problem by always returning consistant and correct data. 

*Note: Currently all Hrotti data is hardcoded. Support for custom data coming soon !*

## Example

For example, say you're developing an app that querries a JSON-RPC call. For example we'll use `eth_blockNumber`. Every time you make a querry to Hrotti, it will give you the same response:
```bash
curl http://localhost:8000/http -X POST -H "Content-Type: application/json" --data '{"method":"eth_blockNumber","params":[],"id":1,"jsonrpc":"2.0"}'
{"jsonrpc":"2.0","id":1,"result":"0x5BAD55"}
```

Hrotti is especially useful for testing subscriptions. Subscriptions are sent on a fixed basis with predictable data. Only incrementing values like the block number:
```bash
wscat -c ws://127.0.0.1:8000/ws
Connected (press CTRL+C to quit)
> {"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["newHeads"]}
< {"id":2,"result":"0x123e","jsonrpc":"2.0"}
< {"jsonrpc":"2.0","method":"eth_subscription","params":{"subscription":"0x123e","result":{"parentHash":"0x00bdd9454ead08e03ad9d1516cdddc7db529de716bf8311a96fc1a2a27889377","sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347","miner":"0x388c818ca8b9251b393131c08a736a67ccb19297","stateRoot":"0xe920ed2fb25543c04e537a6487e5a99c7b9e6516cb36be22c7130d99ba9702ca","transactionsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421","receiptsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421","logsBloom":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000","difficulty":"0x0","number":"0x0","gasLimit":"0x1c9c380","gasUsed":"0x0","timestamp":"0x659b269b","extraData":"0xd883010d05846765746888676f312e32312e34856c696e7578","mixHash":"0x64b6af940d7c2107a0c9d46462fb777cf444da64b055ba6d594568eb50dd9339","nonce":"0x0000000000000000","baseFeePerGas":"0x8d7a7855a","withdrawalsRoot":"0x1b4925152dfdbbb40ca2140d1d2f42a2d505b9e8e9dea2f028463c097141b9ef","blobGasUsed":"","excessBlobGas":"","parentBeaconBlockRoot":"","hash":"0x38484f6cd1a4b8b471e25f3ad52a562a15f8c95cfcaa8cd97d41ca587f69e1ad"}}}
< {"jsonrpc":"2.0","method":"eth_subscription","params":{"subscription":"0x123e","result":{"parentHash":"0x00bdd9454ead08e03ad9d1516cdddc7db529de716bf8311a96fc1a2a27889377","sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347","miner":"0x388c818ca8b9251b393131c08a736a67ccb19297","stateRoot":"0xe920ed2fb25543c04e537a6487e5a99c7b9e6516cb36be22c7130d99ba9702ca","transactionsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421","receiptsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421","logsBloom":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000","difficulty":"0x0","number":"0x1","gasLimit":"0x1c9c380","gasUsed":"0x0","timestamp":"0x659b269b","extraData":"0xd883010d05846765746888676f312e32312e34856c696e7578","mixHash":"0x64b6af940d7c2107a0c9d46462fb777cf444da64b055ba6d594568eb50dd9339","nonce":"0x0000000000000000","baseFeePerGas":"0x8d7a7855a","withdrawalsRoot":"0x1b4925152dfdbbb40ca2140d1d2f42a2d505b9e8e9dea2f028463c097141b9ef","blobGasUsed":"","excessBlobGas":"","parentBeaconBlockRoot":"","hash":"0x38484f6cd1a4b8b471e25f3ad52a562a15f8c95cfcaa8cd97d41ca587f69e1ad"}}}
> 
```

## How to use / Development

Make sure you have [poetry](https://python-poetry.org/) installed. Next, clone this repo and `cd` into it.
```bash
poetry install
poetry shell
uvicorn hrotti.main:app
```
If you are doing development, you can enable hot reloading via `uvicorn hrotti.main:app --reload`.

### Linting

`black`, `isort`, and `flake8` are used for static analysis, linting and formating.

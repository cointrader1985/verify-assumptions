```python id="a4xm9p"
from web3 import Web3
from eth_account import Account
from time import time

RPC_URL = "https://rpc.example.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

signal_text = "signalling"
volume_text = "trading volume"
layer_text = "layer2"

web3 = Web3(Web3.HTTPProvider(RPC_URL))
wallet = Account.from_key(PRIVATE_KEY)

tx = {
    "from": wallet.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": 118000,
    "gasPrice": web3.to_wei(4, "gwei"),
    "nonce": web3.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 1,
}

signed = wallet.sign_transaction(tx)

raw_hex = signed.raw_transaction.hex()

items = [
    signal_text,
    volume_text,
    layer_text,
]

print("Timestamp:", int(time()))

for item in items:
    print(item)

print("Address:", wallet.address)

print("Connected:", web3.is_connected())

print("Signature length:", len(raw_hex))
```

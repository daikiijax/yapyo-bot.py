from web3 import Web3
import time

RPC_URL = 'YOUR_RPC'
PRIVATE_KEY = 'YOUR_PRIVATE_KEY'
CONTRACT_ADDRESS = '0xF03E196040f2B93B8D9DCf010fee9683c76D549c'
MINT_METHOD_ID = '' # ADDRESS BENEFICIARY

web3 = Web3(Web3.HTTPProvider(RPC_URL))
sender_address = web3.eth.account.from_key(PRIVATE_KEY).address

while True:
    try:
        nonce = web3.eth.get_transaction_count(sender_address)
        tx = {
            'from': sender_address,
            'nonce': nonce,
            'to': CONTRACT_ADDRESS,
            'data': MINT_METHOD_ID,
            'value': web3.to_wei('0.0000001', 'ether'),  # VALUE TO BUY TOKEN
            'gas': 300000,
            'gasPrice': web3.to_wei('0.7', 'gwei'), # 1-3 GWEI IS BETTER
            'chainId': web3.eth.chain_id,
        }

        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"hash: https://arbiscan.io/tx/{web3.to_hex(tx_hash)}")

    except Exception as e:
        print(f"Error saat mint: {e}")

    
    time.sleep(...)  # 0-10

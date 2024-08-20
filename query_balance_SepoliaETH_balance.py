import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Accessing the variables
wallet_address = os.getenv("SEPOLIA_WALLET_ADDRESS")
infura_api_key = os.getenv("INFURA_API_KEY")
infura_project_id = os.getenv("INFURA_PROJECT_ID")

# Construct the Infura URL
infura_url = f"https://sepolia.infura.io/v3/14dcde53c42c4ebfaf343d779f8456ad"

# Connect to the Sepolia testnet using the Infura endpoint
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is successful
# in terminal also can:
# curl https://mainnet.infura.io/v3/14dcde53c42c4ebfaf343d779f8456ad \
#     -X POST \
#     -H "Content-Type: application/json" \
#     -d '{"jsonrpc":"2.0","method":"eth_getBalance","params": ["0xE3c2200996a83095099f2b8f69F39d1bBFa33456", "latest"],"id":1}'
    
if web3.is_connected():
    print("Connected to Sepolia testnet")
else:
    print("Connection failed")

# Get the balance in Wei (the smallest unit of Ether)
balance_wei = web3.eth.get_balance(wallet_address)

# Convert the balance from Wei to Ether
balance_ether = web3.from_wei(balance_wei, 'ether')

print(f"Balance of {wallet_address}: {balance_ether} ETH")

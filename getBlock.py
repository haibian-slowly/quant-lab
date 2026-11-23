import os
import requests
from dotenv import load_dotenv

# 1. 从 .env 读取 API Key
load_dotenv()
api_key = os.getenv("HELIUS_API_KEY")

url = f"https://mainnet.helius-rpc.com/?api-key={api_key}"

# Wrapped SOL 的合约地址 (Mint)
sol_mint = "So11111111111111111111111111111111111111112"

# 2. 构造 Helius DAS API 请求
payload = {
    "jsonrpc": "2.0",
    "id": "1",
    "method": "getAsset",
    "params": {
        "id": sol_mint,
        "displayOptions": {
            "showFungible": True
        }
    }
}

# 3. 发送请求并解析
response = requests.post(url, json=payload)
data = response.json()

# 4. 提取价格和小数位 (decimals)
token_info = data["result"]["token_info"]
price = token_info["price_info"]["price_per_token"]
decimals = token_info["decimals"]

print(f"SOL 当前价格: ${price:.2f} USD")
print(f"SOL 小数位 (decimals): {decimals}")
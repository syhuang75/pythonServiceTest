#run.py
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return {"name":"SyOneitem2","description":"這是一個測試用的NFT，採用remix測試，檔案皆放在IPFS上，僅供測試。","image":"https://web-eshop.cdn.hinet.net/eShop%20Images/other/404/EXPIRED.png","external_link":"https://www.google.com","attributes":[{"trait_type":"顏色","value":"綠"},{"trait_type":"文字","value":"SyOne"}]}

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=80)

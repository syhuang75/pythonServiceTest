from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return {"name":"SyOneitem2","description":"這是一個測試用的NFT，採用remix測試，檔案皆放在IPFS上，僅供測試。","image":"ipfs://Qmejnv4RrwviMaTA6LzWeNiWDTJ1y4e2Xm8N46BDYXvQGf","external_link":"https://www.google.com","attributes":[{"trait_type":"顏色","value":"綠"},{"trait_type":"文字","value":"SyOne"}]}

if __name__ == '__main__':
    app.debug = True
    app.run()

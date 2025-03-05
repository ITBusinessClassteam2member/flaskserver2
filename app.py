# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == "__main__":
#     app.run(port=10000, debug=True)
#------------------------------------------------------------
from flask import Flask
import os

app = Flask(__name__)

# 環境変数 PORT を取得（デフォルトは 4000）
port = int(os.getenv("PORT", 4000))

@app.route("/")
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)

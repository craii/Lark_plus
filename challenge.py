# - * - coding:utf-8 - * -
#  作者：Elias Cheung
#  编写时间：2023/6/1  下午5:12
from flask import Flask, jsonify, request
import json

app = Flask(__name__)  # 在当前文件下创建应用


@app.route("/", methods=['POST'])
def index():
    return jsonify(dict(challenge=json.loads(request.data)["challenge"]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6767)

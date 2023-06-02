# - * - coding:utf-8 - * -
#  作者：Elias Cheung
#  编写时间：2023/6/1  下午5:12
from flask import Flask, jsonify, request
from os import getenv
from dotenv import load_dotenv
from views import send_msg, get_message_id, get_open_id, get_message, is_type_valid, connect_claude
import time
import datetime
import json

app = Flask(__name__)  # 在当前文件下创建应用


@app.route("/", methods=['POST'])
def index():
    data = request.data
    data_json = json.loads(data)
    print(f"{datetime.datetime.now()}===\t", "=="*20)
    print("\n文字：", data_json)
    print("===" * 20)
    if get_message_id(data_json) and is_type_valid(data_json):
        open_id = get_open_id(data_json)
        text_query = get_message(data_json)
        result = connect_claude(text_query)
        send_msg(msg=result, receive_id=open_id, msg_type="text")
    return str()


if __name__ == "__main__":
    load_dotenv()
    app.run(host="0.0.0.0", port=getenv("lark_port"))

# - * - coding:utf-8 - * -
#  作者：Elias Cheung
#  编写时间：2023/6/2  下午12:35
import uuid as unique_id
from util import *
from typing import NewType, Union

import requests


ResultMsg = NewType("ResultMsg", Union[AnyStr, str])

def send_msg(msg: str,
             receive_id: str,
             msg_type: str,
             uuid: str=None,
             api: str=None,
             headers: dict=None) -> ResultMsg:
    """
    :param receive_id_type:
    :param msg: 消息, 最终要格式化为json
                消息内容，JSON结构序列化后的字符串。不同msg_type对应不同内容，如"{"text":"test content"}"
    :param receive_id:消息接收者的ID，ID类型应与查询参数receive_id_type 对应；推荐使用 OpenID，获取方式可参考文档如何获取 Open ID？
    :param msg_type:消息类型 包括：text、post、image、file、audio、media、sticker、interactive、share_chat、share_user等，
                    类型定义请参考发送消息Content
    :param uuid: 由开发者生成的唯一字符串序列，用于发送消息请求去重；持有相同uuid的请求1小时内至多成功发送一条消息
    :param api: api
    :param headers: headers
    :return: str-like ResultMsg
    """

    _api = get_api("send_msg") if api is None else api
    _token = get_token()

    req_headers = {"Authorization": f"Bearer {_token}",
                   "Content-Type": "application/json; charset=utf-8"} if headers is None else headers

    req_payload = {"receive_id": receive_id,
                    "msg_type": msg_type,
                    "content": "{" + f'''"{msg_type}": "{msg}"''' + "}",
                    "uuid": f"{unique_id.uuid1() if uuid is None else uuid}"}

    res = requests.post(url=_api, headers=req_headers, data=json.dumps(req_payload)).text
    return res


def connect_claude(msg: str) -> AnyStr:
    load_dotenv()
    _claude = f"http://localhost:{getenv('claude_port')}/claude/chat"
    headers = {"accept": "application/json",
               "Content-Type": "application/json"}
    data = {"prompt": msg}
    raw = requests.post(url=_claude, headers=headers, data=json.dumps(data))
    res = json.loads(raw.text)
    print(f"claude(port:{getenv('claude_port')}):", res)
    print("raw:", raw)
    return res.get("claude", "Claude没有回复，请稍后再试").replace("\n", "\\n")


if __name__ in "__main__":
    pass


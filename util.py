# - * - coding:utf-8 - * -
#  作者：Elias Cheung
#  编写时间：2023/6/2  上午11:23
from os import getenv
from typing import AnyStr, Union
import time

import requests
import json
from dotenv import load_dotenv, set_key


def set_token() -> AnyStr:
    load_dotenv()
    api_url = getenv("token_api")
    data = {"app_id": getenv("app_id"), "app_secret": getenv("app_secret")}
    header = {"Content-Type": "application/json; charset=utf-8"}

    _start = int(time.time())

    res = json.loads(requests.post(url=api_url, headers=header, data=json.dumps(data)).text)

    _expire = _start + res.get("expire", 0)
    token = res.get("tenant_access_token", "")

    set_key(".env", "token_expire", f"{_expire}")
    set_key(".env", "token", f"{token}")

    return token


def is_token_expired() -> bool:
    load_dotenv()
    return int(time.time()) > int(getenv("token_expire"))


def get_token() -> AnyStr:
    load_dotenv()
    return getenv("token") if not is_token_expired() else set_token()


def get_api(api_name: str) -> str:
    load_dotenv()
    return getenv(api_name)


def get_open_id(raw_message: dict) -> str:
    return raw_message.get("event", dict()).get("open_id", "Not a valid open_id")


def get_message(raw_message: dict) -> str:
    return raw_message.get("event", dict()).get("text", "Not a valid message")


def is_type_valid(raw_message: dict) -> bool:
    return raw_message.get("event", dict()).get("msg_type", "Not a valid msg_type") in ("text")


def get_message_id(raw_message: dict) -> Union[str, None]:
    return raw_message.get("uuid", None)


if __name__ in "__main__":
    print(set_token())
    print(is_token_expired())

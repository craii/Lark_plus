# - * - coding:utf-8 - * -
#  作者：Elias Cheung
#  编写时间：2023/5/31  下午2:51
from os import getenv
from typing import Union

from fastapi import FastAPI, Depends, Header, HTTPException, status
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

from slack import client

app = FastAPI()
server_token = getenv("SERVER_TOKEN")
print(server_token)


async def must_token(x_token: Union[str, None] = Header(None)):
    if server_token and x_token != server_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "msg": "must token",
            }
        )


class ClaudeChatPrompt(BaseModel):
    prompt: str


@app.post("/claude/chat", dependencies=[Depends(must_token)])
async def chat(body: ClaudeChatPrompt):
    await client.open_channel()
    await client.chat(body.prompt)

    return {
        "claude": await client.get_reply()
    }

@app.post("/claude/stream_chat", dependencies=[Depends(must_token)])
async def chat(body: ClaudeChatPrompt):
    await client.open_channel()
    await client.chat(body.prompt)

    sr = client.get_stream_reply()

    return StreamingResponse(sr, media_type="text/plain")

@app.post("/claude/reset", dependencies=[Depends(must_token)])
async def chat():
    await client.open_channel()
    await client.chat("请忘记上面的会话内容")

    return {
        "claude": await client.get_reply()
    }


if __name__ == '__main__':
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()

    uvicorn.run(app, host="0.0.0.0", port=getenv("claude_port"))

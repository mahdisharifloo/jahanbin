import os
import sys
import json
import uvicorn
from starlette.responses import FileResponse
from pydantic import BaseModel

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)

from startup import *
from fastapi import FastAPI , Form , Body
from typing import Dict, Any

from utils.logger import Logger

log = Logger("twitter")

app = FastAPI()


# class Base(BaseModel):

#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate_to_json

#     @classmethod
#     def validate_to_json(cls, value):
#         if isinstance(value, str):
#             return cls(**json.loads(value))
#         return value

# class InstagramBase(Base):
#     caption: {"text":str}
#     pk:str
#     user:{"pk":str}
#     username:str

# class NewsBase(Base):
#     pass
#     # data:dict

# class TwitterBase(Base):
#     pass
#     # data:dict
# class TelegramGroup(Base):
#     pass
#     # data:dict


# class TelegramChanel(Base):
#     pass
#     # data:dict


@app.post("/twitter")
async def twitter(data:  Dict[str, Any] = Body(...)):
    if 'data' in data:
        try:
            run_twitter(data=data['data'])
            return {'status': "success"}
        except Exception as e:
            return {'status': "failure", 'error': str(e)}
    else:
        log.warning(f'we have no records')
        return {'status': "empty", 'warning': f'we have no records'}

@app.post("/instagram")
async def instagram(data:  Dict[str, Any] = Body(...)):
    if 'data' in data:
        try:
            run_instagram(data=data['data'])
            return {'status': "success"}
        except Exception as e:
            return {'status': "failure", 'error': str(e)}
    else:
        log.warning(f'we have no records')
        return {'status': "empty", 'warning': f'we have no records'}
    

@app.post("/news")
async def news(data:  Dict[str, Any] = Body(...)):
    if 'data' in data:
        try:
            run_agency(data=data['data'])
            return {'status': "success"}
        except Exception as e:
            return {'status': "failure", 'error': str(e)}
    else:
        log.warning(f'we have no records')
        return {'status': "empty", 'warning': f'we have no records'}

@app.post("/telegram_group")
async def telegram_group(data:  Dict[str, Any] = Body(...)):
    if 'data' in data:
        try:
            run_tel_group(data=data['data'])
            return {'status': "success"}
        except Exception as e:
            return {'status': "failure", 'error': str(e)}
    else:
        log.warning(f'we have no records')
        return {'status': "empty", 'warning': f'we have no records'}


@app.post("/telegram_chanel")
async def telegram_chanel(data:  Dict[str, Any] = Body(...)):
    if 'data' in data:
        try:
            run_tel_chanel(data=data['data'])
            return {'status': "success"}
        except Exception as e:
            return {'status': "failure", 'error': str(e)}
    else:
        log.warning(f'we have no records')
        return {'status': "empty", 'warning': f'we have no records'}




@app.get("/")
async def read_index():
    return FileResponse(f'{root_path}/api/index.html')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10020)

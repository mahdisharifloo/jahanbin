import os
import sys
from datetime import datetime
import uvicorn
from starlette.responses import FileResponse
from starlette.responses import StreamingResponse
import random
from typing import Any, Union,List 

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)

from fastapi import FastAPI
import etl.transform as transform
from utils.logger import Logger
from pydantic import BaseModel
import torch
from transformers import MT5ForConditionalGeneration, MT5Tokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_name_or_path = "persiannlp/mt5-small-parsinlu-sentiment-analysis"
tokenizer = MT5Tokenizer.from_pretrained(model_name_or_path)
model = MT5ForConditionalGeneration.from_pretrained(model_name_or_path)
model.to(device)

log = Logger("sentiment_analysis")

app = FastAPI()

@app.post("/sentiment_analysis")
async def manual_set(prompt) -> Any:
    result = transform.run(device,tokenizer,
                            model,prompt)
    return result


@app.get("/")
async def read_index():
    return FileResponse(f'{root_path}/api/index.html')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10031)

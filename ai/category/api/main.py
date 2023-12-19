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
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch 

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


model_name = "HooshvareLab/bert-fa-base-uncased-clf-persiannews"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.to(device)

log = Logger("nlp")

app = FastAPI()

# @app.post("/category")
# async def manual_set(prompt) -> Any:
#     out = []
#     result = transform.run(model,
#         tokenizer,prompt)
#     # valid_ner = matching_ners(ner,prompt)
#     return result

@app.post("/category")
async def manual_set(prompt) -> Any:
    out = []
    prompt_encoding = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)
    prompt_encoding.to(device)  # Move the input tensor to the device
    result = model(**prompt_encoding)  # Pass the input tensor directly to the model
    predicted_label_index = torch.argmax(result.logits, dim=1).item()
    predicted_label = model.config.id2label[predicted_label_index]

    return predicted_label

@app.get("/")
async def read_index():
    return FileResponse(f'{root_path}/api/index.html')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10036)

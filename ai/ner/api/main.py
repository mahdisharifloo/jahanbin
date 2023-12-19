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
from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification  # for pytorch
from transformers import TFAutoModelForTokenClassification  # for tensorflow
from transformers import pipeline
import torch 

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



model_name_or_path = "HooshvareLab/bert-fa-zwnj-base-ner" 
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForTokenClassification.from_pretrained(model_name_or_path)  # Pytorch
# model = TFAutoModelForTokenClassification.from_pretrained(model_name_or_path)  # Tensorflow
model.to(device)

log = Logger("nlp")

app = FastAPI()

class NERItem(BaseModel):
    entity : Union[str, None] = None 
    score: Union[float, None] = None 
    index: Union[int, None] = None 
    word: Union[str, None] = None 
    start: Union[int, None] = None  
    end: Union[int, None] = None  

# def matching_ners(ner:List[dict],prompt):
#     words = prompt.split(' ')
#     valid_ners = []
#     for i,item in enumerate(ner):
#         pop_index = []
#         if i+1 < len(ner) and  ner[i+1]['start'] - item['end'] == 1 :
#             if item['word'] not in words:
#                 item['word'] = item['word'].replace('#',"")
#                 ner[i+1]['word'] = ner[i+1]['word'].replace('#',"")
#                 v_ner = {'entity':item['entity'],
#                         'index':ner[i+1]['index'],
#                         'word':item['word'] + ner[i+1]['word'],
#                         'start':item['start'],
#                         'end':ner[i+1]['end']
#                         }
#                 pop_index.append(i+1)
#             else:
#                 item['word'] = item['word'].replace('#',"")
#                 ner[i+1]['word'] = ner[i+1]['word'].replace('#',"")
#                 v_ner = {'entity':item['entity'],
#                         'index':ner[i+1]['index'],
#                         'word':item['word'] + ' ' + ner[i+1]['word'],
#                         'start':item['start'],
#                         'end':ner[i+1]['end']
#                         }
#                 pop_index.append(i+1)
#             if i+1 < len(ner) and i+2<len(ner) and  ner[i+2]['start'] - ner[i+1]['end']  == 0 :
#                 ner[i+2]['word'] = ner[i+2]['word'].replace('#',"")
#                 v_ner = {'entity':item['entity'],
#                         'index':ner[i+2]['index'],
#                         'word':item['word'] + ner[i+1]['word'] + ner[i+2]['word'],
#                         'start':item['start'],
#                         'end':ner[i+2]['end']
#                         }
#                 pop_index.append(i+2)
#             if i+1 < len(ner) and i+2<len(ner) and i+3<len(ner) and  ner[i+3]['start'] - ner[i+2]['end']  == 0 :
#                 ner[i+3]['word'] = ner[i+3]['word'].replace('#',"")
#                 v_ner = {'entity':item['entity'],
#                         'index':ner[i+3]['index'],
#                         'word':item['word'] + ner[i+1]['word'] + ner[i+2]['word'] + ner[i+3]['word'],
#                         'start':item['start'],
#                         'end':ner[i+3]['end']
#                         }
#                 pop_index.append(i+3)
            
#             for c in pop_index:
#                 ner.pop(c)
#             valid_ners.append(v_ner)
            
#         else:
#             valid_ners.append(item)
#     return valid_ners

@app.post("/ner",response_model=List[NERItem])
async def manual_set(prompt) -> Any:
    out = []
    ner = transform.run(model,
        tokenizer,device,prompt)
    # valid_ner = matching_ners(ner,prompt)
    return ner


@app.get("/")
async def read_index():
    return FileResponse(f'{root_path}/api/index.html')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10035)

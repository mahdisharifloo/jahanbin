import pandas as pd
import re 
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np

labels = ["entails", "contradicts", "neutral"]
model_name_or_path = "persiannlp/parsbert-base-parsinlu-entailment"
model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path,)

def model_predict(text_a, text_b):
    features = tokenizer( [(text_a, text_b)], padding="max_length", truncation=True, return_tensors='pt')
    output = model(**features)
    logits = output[0]
    probs = torch.nn.functional.softmax(logits, dim=1).tolist()
    idx = np.argmax(np.array(probs))
    return (labels[idx], probs)


clean = 'فردا جمع بشید میدون انقلاب تا اعتراضمونو نشون بدیم'
q = 'این متن دعوت به اعتراض است'

t1 = model_predict(
        clean ,
        q
    )
print(t1)
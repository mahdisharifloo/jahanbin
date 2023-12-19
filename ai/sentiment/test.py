import torch
from transformers import MT5ForConditionalGeneration, MT5Tokenizer
import numpy as np

model_name_or_path = "persiannlp/mt5-small-parsinlu-sentiment-analysis"
tokenizer = MT5Tokenizer.from_pretrained(model_name_or_path)
model = MT5ForConditionalGeneration.from_pretrained(model_name_or_path)


def model_predict(text_a, text_b):
    features = tokenizer( [(text_a, text_b)], padding="max_length", truncation=True, return_tensors='pt')
    output = model(**features)
    logits = output[0]
    probs = torch.nn.functional.softmax(logits, dim=1).tolist()
    idx = np.argmax(np.array(probs))
    print(labels[idx], probs)


def run_model(context, query, **generator_args):
    input_ids = tokenizer.encode(context + "<sep>" + query, return_tensors="pt")
    res = model.generate(input_ids, **generator_args)
    output = tokenizer.batch_decode(res, skip_special_tokens=True)
    print(output)
    return output


run_model(
    "یک فیلم ضعیف بی محتوا بدون فیلمنامه . شوخی های سخیف .",
    "نظر شما در مورد داستان، فیلمنامه، دیالوگ ها و موضوع فیلم  لونه زنبور چیست؟"
)
print('model loaded successfully!!')
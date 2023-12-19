import torch
from transformers import MT5ForConditionalGeneration, MT5Tokenizer
import numpy as np


# def model_predict(text_a, text_b):

#     features = tokenizer( [(text_a, text_b)], padding="max_length", truncation=True, return_tensors='pt')
#     output = model(**features)
#     logits = output[0]
#     probs = torch.nn.functional.softmax(logits, dim=1).tolist()
#     idx = np.argmax(np.array(probs))
#     print(labels[idx], probs)


def run_model(device,tokenizer,
                model,context, query, **generator_args):

    input_ids = tokenizer.encode(context + "<sep>" + query, return_tensors="pt").to(device)
    res = model.generate(input_ids, **generator_args)
    output = tokenizer.batch_decode(res, skip_special_tokens=True)
    print(output)
    return output

def run(device,tokenizer,
                model ,prompt):
    query = "نظر شما به صورت کلی در مورد این خبر چیست؟"
    return run_model(device,tokenizer,
                        model ,prompt,query)
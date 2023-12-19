from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification  # for pytorch
from transformers import TFAutoModelForTokenClassification  # for tensorflow
from transformers import pipeline
import copy

def cleaning_ners(ner):
    ner_copy = copy.copy(ner)
    delete_items = []
    for i,item in enumerate(ner):
        clean_word = item['word'].replace("#","")
        item['word'] = clean_word
        ner[i]['word'] = clean_word
        ner_copy[i]['word'] = clean_word
        if i>0 :
            if item['start']-ner[i-1]['end']==1:
                if item['entity'].split('-')[1] == ner[i-1]['entity'].split('-')[1] :
                    ner_copy[i]["word"] = ner[i-1]['word']  + ' ' + item['word'] 
                    ner_copy[i]["start"] = ner[i-1]["start"]
                    delete_items.append(i-1)
            if item['start']-ner[i-1]['end']==0:
                if item['entity'].split('-')[1] == ner[i-1]['entity'].split('-')[1] :
                    ner_copy[i]["word"] = ner[i-1]['word']  + item['word'] 
                    ner_copy[i]["start"] = ner[i-1]["start"]
                    delete_items.append(i-1)
    for d in sorted(delete_items,reverse=True):
        del ner_copy[d]
    return ner_copy


def run(model,
        tokenizer,device,prompt):

    nlp = pipeline("ner", model=model, tokenizer=tokenizer,device=device)
    ner_results = nlp(prompt)
    result = cleaning_ners(ner_results)
    return result
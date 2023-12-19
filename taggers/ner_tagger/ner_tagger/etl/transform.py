import json
import requests
from utils.logger import Logger
import utils.config as cfg

log = Logger('ner')

def get_ner_response(payload):
    payload = payload.replace('\n','\\n')
    payload = payload.replace('\t','\\t')
    if len(payload) > 1000:
        payload = payload[:1000]
    querystring = {"prompt":payload.encode('utf-8')}
    url = f"http://{cfg.NER_HOST}:10030/ner"
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        log.error(f'response error {response.status_code}')


def run(instagram  , twitter , telegram_group  , 
        telegram_channel , news_agency):
    for d in instagram:
        d['ner'] = get_ner_response(d['clean_context'])

    for d in twitter:
        d['ner'] = get_ner_response(d['clean_context'])

    for d in telegram_group:
        d['ner'] = get_ner_response(d['clean_context'])

    for d in telegram_channel:
        d['ner'] = get_ner_response(d['clean_context'])

    for d in news_agency:
        d['ner'] = get_ner_response(d['clean_context'])
    
    return instagram  , twitter , telegram_group  , \
        telegram_channel , news_agency

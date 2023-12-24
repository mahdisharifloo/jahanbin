import json
import requests
from utils.logger import Logger
import utils.config as cfg

log = Logger('sentiment')

def get_sentiment_response(payload):
    payload = payload.replace('\n','\\n')
    payload = payload.replace('\t','\\t')
    if len(payload) > 1000:
        payload = payload[:1000]
    querystring = {"prompt":payload.encode('utf-8')}
    url = f"http://{cfg.SENTIMENT_HOST}:10031/sentiment_analysis"
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return json.loads(response.text)[0]
    else:
        log.error(f'response error {response.status_code}')


def run(instagram  , twitter , telegram_group  , 
        telegram_channel , news_agency):
    for d in instagram:
        d['sentiment'] = get_sentiment_response(d['clean_context'])

    for d in twitter:
        d['sentiment'] = get_sentiment_response(d['clean_context'])

    for d in telegram_group:
        d['sentiment'] = get_sentiment_response(d['clean_context'])

    for d in telegram_channel:
        d['sentiment'] = get_sentiment_response(d['clean_context'])

    for d in news_agency:
        d['sentiment'] = get_sentiment_response(d['clean_context'])
    
    return instagram  , twitter , telegram_group  , \
        telegram_channel , news_agency

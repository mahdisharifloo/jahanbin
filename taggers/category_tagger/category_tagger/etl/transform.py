import json
import requests
from utils.logger import Logger
import utils.config as cfg
import re 

log = Logger('category')



def clean_caption(caption):
    if caption:
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\u3030"
                                "]+", flags=re.UNICODE)
        caption = emoji_pattern.sub(r' ', caption)
        caption = caption.replace('آ', 'ا')
        caption = caption.replace(':', ' ')
        caption = caption.replace('=', ' ')
        caption = caption.replace('.',' ')
        caption = caption.lower()
        caption = re.sub('#(_*[آ-ی0-9a-z_]*_*\s*)', '', caption)
        caption = re.sub('[^A-Za-z0-9آ-ی #@\n/_.]+', '', caption)
        caption = " " + caption + " "

        punc='!"”“#$%&\'()*+,./:;<=>?@[\\]^_`{|}~-0123456789۰۱۲۳۴۵۶۷۸۹abcdefghijklmnopqrstuvwxyz'
        for ch in punc:
            caption = caption.replace(ch, '')
        caption=caption.replace('‌','')
        return caption.strip()


def get_category_response(payload):
    # payload = payload.replace('\n','\\n')
    # payload = payload.replace('\t','\\t')
    if len(payload) > 1000:
        payload = payload[:1000]

    querystring = {"prompt":payload}
    url = f"http://{cfg.CATEGORY_HOST}:10034/category"
    headers = {"accept": "application/json"}

    response = requests.post(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        log.error(f'response error {response.status_code}')


def run(instagram  , twitter , telegram_group  , 
        telegram_channel , news_agency):
    
    if instagram:
        for d in instagram:
            d['category'] = get_category_response(d['clean_context'])
    if twitter:
        for d in twitter:
            d['category'] = get_category_response(d['clean_context'])
    if telegram_group:
        for d in telegram_group:
            d['category'] = get_category_response(d['clean_context'])
    if telegram_channel:
        for d in telegram_channel:
            d['category'] = get_category_response(d['clean_context'])
    if news_agency:
        for d in news_agency:
            d['category'] = get_category_response(d['clean_context'])
    
    return instagram  , twitter , telegram_group  , \
        telegram_channel , news_agency

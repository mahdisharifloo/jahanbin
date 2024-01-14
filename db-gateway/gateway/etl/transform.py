from datetime import datetime
import pandas as pd 
import re 




def clean_caption(caption):
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
    # taking the whole caption and remove extra characters and returning split caption(cleaned_caption)
    if pd.isna(caption):
        return []
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



def transform_instagram(d):
    d['created_at'] = datetime.now()
    if ['caption.text']:
        d['clean_context'] = clean_caption(d['caption.text'])
    else:
        d['clean_context'] = ''
    return d

def transform_tel_group(d):
    d['created_at'] = datetime.now()
    # date_format = '%Y-%m-%d %H:%M:%S'
    # d['created_at'] = datetime.strptime(d['date'], date_format)
    if d['message']:
        d['clean_context'] = clean_caption(d['message'])
    else:
        d['clean_context'] = ''
    return d

def transform_tel_chanel(d):
    d['created_at'] = datetime.now()
    # date_format = '%Y-%m-%d %H:%M:%S'
    # d['created_at'] = datetime.strptime(d['date'], date_format)
    if d['message']:
        d['clean_context'] = clean_caption(d['message'])
    else:
        d['clean_context'] = ''
    return d

def transform_twitter(d):
    # date_format = '%Y-%m-%d %H:%M:%S'
    # d['created_at'] = datetime.strptime(d['created_at'], date_format)
    d['created_at'] = datetime.now()
    if d['full_text']:
        d['clean_context'] = clean_caption(d['full_text'])
    else:
        d['clean_context'] = ''
    return d

def transform_agency(d):
    d['created_at'] = datetime.now()
    # date_format = '%Y-%m-%d %H:%M:%S'
    # d['created_at'] = datetime.strptime(d['created_at'], date_format)
    if d['content']:
        d['clean_context'] = clean_caption(d['content'])
    else:
        d['clean_context'] = ''
    return d

import os
import time
import etl.extract as extract
import etl.load as load
import etl.transform as transform
from utils.logger import Logger
from datetime import datetime,timedelta

log = Logger("data_fetch")
os.environ['TZ'] = 'UTC'
time.tzset()

def run(instagram  , twitter , telegram_group  , telegram_channel , news_agency):
    """
    Extract, transform and load Data
    """
    parsed_instagram  , parsed_twitter , \
    parsed_telegram_group  , parsed_telegram_channel , parsed_news_agency = transform.run(
        instagram  , twitter , telegram_group  , 
        telegram_channel , news_agency)
    
    result = load.run(parsed_instagram ,
                      parsed_twitter ,
                      parsed_telegram_group,
                      parsed_telegram_channel,
                      parsed_news_agency)
    return result



if __name__ == '__main__':
    while True:
        instagram  , twitter , telegram_group  , telegram_channel , news_agency = extract.run(1)
        try:
            run(instagram  , twitter , telegram_group  , telegram_channel , news_agency)
            log.info("data tagger Ran Successfully")
        except Exception as e:
            log.error(e)
        print('working done')
        time.sleep(0.2)

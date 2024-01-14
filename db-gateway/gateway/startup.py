import os
import time

import etl.transform as transform
import etl.load as load
from utils.logger import Logger
from datetime import datetime
import etl.extract as extract  


log = Logger("twitter")
os.environ['TZ'] = 'UTC'
time.tzset()

def run_instagram(data):
    # platform = 'instagram'
    parsed_data = transform.transform_instagram(data)
    result = load.load_instagram(parsed_data)
    return result 

def run_tel_group(data):
    # platform = 'tel_group'
    parsed_data = transform.transform_tel_group(data)
    result = load.load_tel_group(parsed_data)
    return result 

def run_tel_chanel(data):
    # platform = 'tel_chanel'
    parsed_data = transform.transform_tel_chanel(data)
    result = load.load_tel_chanel(parsed_data)
    return result 

def run_twitter(data):
    # platform = 'twitter'
    parsed_data = transform.transform_twitter(data)
    result = load.load_twitter(parsed_data)
    return result 

def run_agency(data):
    # platform = 'agency'
    parsed_data = transform.transform_agency(data)
    result = load.load_agency(parsed_data)
    return result 




if __name__ == '__main__':
    instagram , tel_group , tel_chanel , twitter , agency = extract.run()
    
    instagram , tel_group , tel_chanel , twitter , agency = transform.run(
        instagram , tel_group , tel_chanel ,twitter , agency )
    
    load.run(instagram , tel_group , tel_chanel ,twitter , agency )

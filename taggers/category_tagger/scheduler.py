import os
import time

import etl.extract as extract
import etl.load as load
import etl.transform as transform
from utils.logger import Logger
from datetime import datetime,timedelta
from time import sleep

log = Logger("data_fetch")
os.environ['TZ'] = 'UTC'
time.tzset()


def run(data):
    """
    Extract, transform and load Data
    """
    if data:
        parsed_data = transform.run(data)
        result = load.run(data=parsed_data)
        return result
    else:
        log.error(f"Extract data failed")


if __name__ == '__main__':
    while True:

        delta_blow = datetime.now() - timedelta(minutes=1)
        delta_head = datetime.now()
        data = extract.run(delta_blow=delta_blow , delta_head=delta_head) 
        result = run(data)
        sleep(60)
from utils.mongo import Mongo
from utils.logger import Logger
from datetime import datetime, timedelta, date

log = Logger("Filtering")

class instagramModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'instagram_posts'
    _db_name = 'data_pipline'

class TwitterModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'twitter_posts'
    _db_name = 'data_pipline'


class TelegramGroupModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'telegram_group_posts'
    _db_name = 'data_pipline'


class TelegramChannelModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'telegram_channel_posts'
    _db_name = 'data_pipline'

class NewsAgencyModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'news_agency_posts'
    _db_name = 'data_pipline'



def run(count):
    instagram_model = instagramModel()
    twitter_model = TwitterModel()
    telegram_group_model = TelegramGroupModel()
    telegram_channel_model = TelegramChannelModel()
    news_agency_model = NewsAgencyModel()
    today = datetime.combine(date.today(), datetime.min.time())  + timedelta(days=1) 
    day_limit = 120
    query = {
    '$and': [
        {"created_at": {"$gt": today - timedelta(days=day_limit)}},
        {"created_at": {"$lte": today}},
        {"category":None}

]}


    #initalizing iterators 
    instagram_posts_iterator = instagram_model.collection.find(query).limit(count)
    twitter_posts_iterator = twitter_model.collection.find(query).limit(count)
    telegram_group_posts_iterator = telegram_group_model.collection.find(query).limit(count)
    telegram_channel_posts_iterator = telegram_channel_model.collection.find(query).limit(count)
    news_agency_posts_iterator = news_agency_model.collection.find(query).limit(count)
    
    # get data from 5 collections
    instagram_posts = [doc for doc in instagram_posts_iterator]
    twitter_posts = [doc for doc in twitter_posts_iterator]
    telegram_group_posts = [doc for doc in telegram_group_posts_iterator]
    telegram_channel_posts = [doc for doc in telegram_channel_posts_iterator]
    news_agency_posts = [doc for doc in news_agency_posts_iterator]
    
    return  instagram_posts ,\
            twitter_posts,\
            telegram_group_posts,\
            telegram_channel_posts,\
            news_agency_posts

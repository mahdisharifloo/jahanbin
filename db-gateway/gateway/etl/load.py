from utils.mongo import Mongo
from pymongo import UpdateOne

class LifewebPostModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'lifeweb_post'
    _db_name = 'data_pipline'

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



def load_instagram(d):
    # data = [d]
    instagram_posts_model = instagramModel()
    # instagram_operations = [UpdateOne({'pk': d['pk']}, {'$set': d}, upsert=True) for d in data]
    # result = instagram_posts_model.collection.bulk_write(instagram_operations)
    result = instagram_posts_model.insert_one(d)
    return result

def load_tel_group(d):
    # data = [d]
    telegram_group_posts_model = TelegramGroupModel()
    # telegram_group_operations = [UpdateOne({'id': d['id']}, {'$set': d}, upsert=True) for d in data]
    # result = telegram_group_posts_model.collection.bulk_write(telegram_group_operations)
    result = telegram_group_posts_model.insert_one(d)
    return result

def load_tel_chanel(d):
    # data = [d]
    telegram_channel_posts_model = TelegramChannelModel()
    # telegram_channel_operations = [UpdateOne({'id': d['id']}, {'$set': d}, upsert=True) for d in data]
    # result = telegram_channel_posts_model.collection.bulk_write(telegram_channel_operations)
    result = telegram_channel_posts_model.insert_one(d)
    return result

def load_twitter(d):
    # data = [d]
    twitter_posts_model = TwitterModel()
    # twitter_operations = [UpdateOne({'id': d['id']}, {'$set': d}, upsert=True) for d in data]
    # result = twitter_posts_model.collection.bulk_write(twitter_operations)
    result = twitter_posts_model.insert_one(d)
    return result

def load_agency(d):
    # data = [d]
    news_agency_posts_model = NewsAgencyModel()
    # news_agency_operations = [UpdateOne({'title': d['title']}, {'$set': d}, upsert=True) for d in data]
    # result = news_agency_posts_model.collection.bulk_write(news_agency_operations)
    result = news_agency_posts_model.insert_one(d)
    return result    
from pymongo import UpdateOne
from utils.mongo import Mongo
from utils.logger import Logger

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


def run(instagram  , 
        twitter ,
        telegram_group  , 
        telegram_channel , 
        news_agency):

    instagram_model = instagramModel()
    instagram_operations = [
        UpdateOne({'_id': d['_id']}, 
        {'$set': {'sentiment': d['sentiment']}}, upsert=True) for d in instagram]
    result_instagram = instagram_model.collection.bulk_write(instagram_operations)


    twitter_model = TwitterModel()
    twitter_operations = [
        UpdateOne({'_id': d['_id']}, 
        {'$set': {'sentiment': d['sentiment']}}, upsert=True) for d in twitter]
    result_twitter = twitter_model.collection.bulk_write(twitter_operations)


    telegram_group_model = TelegramGroupModel()
    telegram_group_operations = [
        UpdateOne({'_id': d['_id']}, 
        {'$set': {'sentiment': d['sentiment']}}, upsert=True) for d in telegram_group]
    result_telegram_group = telegram_group_model.collection.bulk_write(telegram_group_operations)


    telegram_channel_model = TelegramChannelModel()
    telegram_channel_operations = [
        UpdateOne({'_id': d['_id']}, 
        {'$set': {'sentiment': d['sentiment']}}, upsert=True) for d in telegram_channel]
    result_telegram_channel = telegram_channel_model.collection.bulk_write(telegram_channel_operations)


    news_agency_model = NewsAgencyModel()
    news_agency_operations = [
        UpdateOne({'_id': d['_id']}, 
        {'$set': {'sentiment': d['sentiment']}}, upsert=True) for d in news_agency]
    result_news_agency = news_agency_model.collection.bulk_write(news_agency_operations)

    return  result_instagram,\
            result_twitter,\
            result_telegram_group,\
            result_telegram_channel,\
            result_news_agency
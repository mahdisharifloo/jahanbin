import os
import sys
from fastapi import Depends
from fastapi import APIRouter

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)

from models.auth import *
from controllers.auth import *
from controllers.operations import NewsAgencyOps
from utils.logger import Logger
log = Logger("access_api")


router = APIRouter()
tags_metadata = [
    {"name": "Instagram", "description": "Endpoints related to instagram"},
    {"name": "Twitter", "description": "Endpoints related to twitter"},
    {"name": "NewsAgency", "description": "Endpoints related to news_agency"},
    {"name": "TelegramChannels", "description": "Endpoints related to telegram_channels"},
    {"name": "TelegramGroups", "description": "Endpoints related to telegram_groups"},
    {"name": "B2B", "description": "Endpoints related to worker-related functionality."},
    {"name": "Login", "description": "Endpoints related to loging functionality."},
]

ops = NewsAgencyOps()


@router.get("/news_agency/records", tags=["NewsAgency"])
async def records_end_point(sentiment='', category='',
                            inteligence_service_category='',
                            time_filtering="6m", count=10,
                            current_user: User = Depends(
                                get_current_active_user)
                            ):

    data = ops.get_records(sentiment, category,
                           inteligence_service_category,
                           time_filtering, count)
    return {"news": data}


@router.post("/news_agency/add_info_service_tag", tags=["NewsAgency"])
async def info_service_tag_end_point(record_id, label,
                                     current_user: User = Depends(get_current_active_user)):
    status = ops.add_info_service_tag(record_id, label)
    return {"status": status}


@router.get("/news_agency/get_statistics", tags=["NewsAgency"])
async def get_statistics_end_point(current_user: User = Depends(get_current_active_user)):
    data = ops.get_statistics()
    return data 

@router.get("/news_agency/get_news", tags=["NewsAgency"])
async def news_end_point(page=1,
                   sentiment='',
                   category='',
                   inteligence_service_category='',
                   time_filtering="6m",
                   current_user: User = Depends(get_current_active_user)
                   ):
    data, pages = ops.get_news(page, sentiment, category,
                           inteligence_service_category,
                           time_filtering)
    return {"news": data, "pages": pages}


@router.get("/news_agency/search", tags=["NewsAgency"])
async def search_news_end_point(query, page=1, time_filtering="6m",
                                current_user: User = Depends(get_current_active_user)):
    data, pages = ops.search_news(query,page,time_filtering)
    return {"news": data, "pages": pages}


@router.get("/news_agency/sunburst_chart_data", tags=["NewsAgency"])
async def sunburst_end_point(charts_time_filter=None,
                             current_user: User = Depends(get_current_active_user)):
    data = ops.get_sunburst_chart_data(charts_time_filter)
    return data


@router.get("/news_agency/last_news", tags=["NewsAgency"])
async def last_news_end_point(count=5,
                            current_user: User = Depends(
                                get_current_active_user)
                            ):
    data = ops.last_news(count)
    return {"news": data}

@router.get("/news_agency/rule_base_info_service", tags=["NewsAgency"])
async def rule_base_info_service_end_point(caption=None,
                             current_user: User = Depends(get_current_active_user)):
    data = ops.get_rule_base_info_service_tag(caption)
    return data


@router.get("/news_agency/get_tag_cload", tags=["NewsAgency"])
async def get_tag_cload_end_point(days_ago=30,
                             current_user: User = Depends(get_current_active_user)):
    data = ops.generate_word_frequencies(int(days_ago))
    return data

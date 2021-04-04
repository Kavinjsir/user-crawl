# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    # 'Cookie': '_T_WM=13701d9e25d451e1c768ef4b080359e4; SUB=_2A25NN7DjDeRhGeRL6lcS9S3Ewj-IHXVu29CrrDV6PUJbkdAfLRH3kW1NUzVErD0oLGiVoyUihYjQJi7mCwlCmRF2; SCF=AoxwRfZepDgelBvXL4pw4IKC_aOMDL-ji87YW69SvNAFQayGzGcfndXvnTHHU0u97cW2tiqV8izgHLPxiC0l6NY.; SSOLoginState=1614004403'
    # 'Cookie':'SCF=AolrjEdbs-UqesktjmOO4UaKyvRKHQKEYFtQeUuICNrCA67tC1ki7wPJryJ4WqYRTwmKY4qfxaXYykr-5LuP27g.; SUB=_2A25NMhaODeRhGeRL6lcS9S3Ewj-IHXVu3LrGrDV6PUJbktAKLXDzkW1NUzVErI4GEh03YCOIyp9KzZuPx3NNU0Kr; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWql6Bk8xTV2sNdSyM0qW8W5NHD95QESK2fe0-01h.0Ws4Dqcj.i--Ri-zRiKysi--ci-82iKyhi--NiKnpi-8si--NiKnpi-8F; SSOLoginState=1614178014; _T_WM=d925477bf0582f4c06202265c2c8b8da'
    'Cookie':'SCF=AolrjEdbs-UqesktjmOO4UaKyvRKHQKEYFtQeUuICNrCA67tC1ki7wPJryJ4WqYRTwmKY4qfxaXYykr-5LuP27g.; SUB=_2A25NMhaODeRhGeRL6lcS9S3Ewj-IHXVu3LrGrDV6PUJbktAKLXDzkW1NUzVErI4GEh03YCOIyp9KzZuPx3NNU0Kr; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWql6Bk8xTV2sNdSyM0qW8W5NHD95QESK2fe0-01h.0Ws4Dqcj.i--Ri-zRiKysi--ci-82iKyhi--NiKnpi-8si--NiKnpi-8F; SSOLoginState=1614178014; _T_WM=d925477bf0582f4c06202265c2c8b8da'
}


CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}

# MONGO_HOST = '127.0.0.1'
# MONGO_PORT = 27017
MONGO_URL = 'mongodb+srv://crawler:ThRZb0wCj0YHkqy6@sunday.jep2j.mongodb.net/hualuzi'


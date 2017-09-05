import os
import sys
from newspaper import Article

# import comment package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scraper'))

import cnn_news_scraper
from cloudamqp_client import CloudAMQPClient

# use your own queue
DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://zvzoktui:sRxElb4hBYLUoMLrYlHb64SKfYI9_PNu@wasp.rmq.cloudamqp.com/zvzoktui"
DEDUPE_NEWS_TASK_QUEUE_NAME = "news-dedupe-queue"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://mitqwttx:uZ7OmxAZxJSfAJyO0nbauhI_YENz7SEw@crane.rmq.cloudamqp.com/mitqwttx"
SCRAPE_NEWS_TASK_QUEUE_NAME = "news-scrape-queue"

SLEEP_TIME_IN_SECONDS = 5

deduper_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print 'message is broken'
        return

    task = msg
    text = None


    article = Article(task['url'])
    article.download()
    article.parse()

    task['text'] = article.text.encode('utf-8')
    deduper_news_queue_client.send_message(task)

""" old way of scraping news
    
    if task['source'] == 'cnn':
        print 'scraping CNN news'
        text = cnn_news_scraper.extract_news(task['url'])
    else:
        print 'News Source [%s] is not supported.' % task['source']

    task['text'] = text

    deduper_news_queue_client.send_message(task)
"""

while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.get_message()
        if msg is not None:
            try: 
                handle_message(msg)
            except Exception as e:
                print e #coding=utf-8
                pass # pass the exception, continue reading new news

        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)

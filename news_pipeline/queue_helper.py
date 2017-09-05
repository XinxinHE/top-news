import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import news_api_client
from cloudamqp_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://mitqwttx:uZ7OmxAZxJSfAJyO0nbauhI_YENz7SEw@crane.rmq.cloudamqp.com/mitqwttx"
SCRAPE_NEWS_TASK_QUEUE_NAME = "news-scrape-queue"

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://zvzoktui:sRxElb4hBYLUoMLrYlHb64SKfYI9_PNu@wasp.rmq.cloudamqp.com/zvzoktui"
DEDUPE_NEWS_TASK_QUEUE_NAME = "news-dedupe-queue"

def clearQueue(queue_url, queue_name):
    scrape_news_queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.get_message()
            if msg is None:
                print "Cleared %d messages." %num_of_messages
                return
            num_of_messages += 1

if __name__ == "__main__":
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    clearQueue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
    
import cnn_news_scraper as scraper 

EXPECTED_NEWS = "With dire warnings of tornadoes, torrential downpours and days of flooding to come, broad swaths of southeast Texas were littered with uprooted trees, toppled signs, flagpoles that snapped like toothpicks and clusters of bricks peeled like scabs from walls and rooftops."
CNN_NEWS_URL = "http://www.cnn.com/2017/08/26/us/hurricane-harvey-landfall/index.html"

def test_basic():
    print "start scraping: "
    news = scraper.extract_news(CNN_NEWS_URL)

    print news
    assert EXPECTED_NEWS in news
    print 'test_basic passed!'

if __name__ == "__main__":
    test_basic()

""" Mongo Client Unit Test """

import mongodb_client as client

def test_basic():
    """ Test for mongoDB client """
    database = client.get_db('test')
    database.testCollection.drop()
    assert database.testCollection.count() == 0
    database.testCollection.insert({'test': 1, 'hello': 'world'})
    assert database.testCollection.count() == 1
    # database.testCollection.drop()
    # assert database.testCollection.count() == 0
    print 'test_basic passed.'

if __name__ == "__main__":
    test_basic()
    

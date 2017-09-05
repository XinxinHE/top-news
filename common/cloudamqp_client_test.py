""" Cloud AMQP Client class test """
from cloudamqp_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://ubbgnavv:XuETa4VLsIYv6Z0GJ8aPF71so3sii2Ri@wasp.rmq.cloudamqp.com/ubbgnavv"
TEST_QUEUE_NAME = "bittiger-project"


def test_basic():
    """ Send messages and receive messages """
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sent_msg = {"test": "test"}
    client.send_message(sent_msg)
    received_msg = client.get_message()

    assert sent_msg == received_msg
    print "test_basic passed."


if __name__ == "__main__":
    test_basic()

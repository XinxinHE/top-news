""" CloudAMQPClient class Definition """
import json
import pika


class CloudAMQPClient(object):
    """ Class definition """

    def __init__(self, cloud_amqp_url, queue_name):
        self.cloud_amqp_url = cloud_amqp_url
        self.queue_name = queue_name
        self.params = pika.URLParameters(cloud_amqp_url)
        self.params.socket_time_timeout = 3
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, message):
        """ Send messages to AMQP """
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=json.dumps(message))  # json to string
        print "Sent message to %s : %s" % (self.queue_name, message)

    def get_message(self):
        """ Get messages from AMQP """
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            # check if there is any message
            print 'Received message from %s: %s' % (self.queue_name, body)
            # deleted only when received a delivery_tag
            self.channel.basic_ack(method_frame.delivery_tag)
            return json.loads(body)
        print 'No message returned.'
        return None

    # program needs to response to heartbeat
    # BlockingConnection.sleep is a safer way to sleep than time.sleep()
    def sleep(self, seconds):
        """ Sleep for seconds """
        self.connection.sleep(seconds)

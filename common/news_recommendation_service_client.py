import pyjsonrpc

URL = "http://localhost:5050/"

client = pyjsonrpc.HttpClient(url=URL)

def getPreferenceForUser(userId):
    """ Call rpc function from ../news_recommendation_service/recommendation_service.py"""
    preference = client.call('getPreferenceForUser', userId)
    print "Preference list: %s" % str(preference)
    return preference
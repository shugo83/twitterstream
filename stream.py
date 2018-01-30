from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import configparser
import os
config = configparser.ConfigParser()
config.read('config.ini')
access_token = config['DEFAULT']['access_token']
access_token_secret = config['DEFAULT']['access_token_secret']
consumer_key = config['DEFAULT']['consumer_key']
consumer_secret = config['DEFAULT']['consumer_secret']
directory='saves'
if not os.path.exists(directory):
    os.makedirs(directory)
count=50
kwarg=sys.argv[1]
kwarg=kwarg.strip("'")
print(kwarg)
name=kwarg+str(count)+'.txt'
location=directory+'/'+name
print(location)
class StdOutListener(StreamListener):
    def __init__(self):
        self.count=0
    def on_data(self, data):
#        print (data)
        self.count=self.count+1
        print(self.count)
        if self.count>count:
            sys.exit(0)
        with open(location, 'a') as f:
                f.write(data)
                return True
        return True

    def on_error(self, status):
        print (status)
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=[kwarg])

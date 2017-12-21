#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status
        return True # Don't kill the stream                                 # new code

    def on_timeout(self):                                                   # new code
        return True # Don't kill the stream                                 # new code

def streamingTwitter():
    try:
	    #This line filter Twitter Streams
        #SW corner first, East/West point first (longitude)
	    #US stream.filter(locations = [-125.011, 24.047, -67.3, 49.458])
        stream.filter(locations = [-125.011, 24.047, -67.3, 49.458])

    except UnicodeDecodeError:
    	#Skip tweets with UnicodeDecodeError and recall streamingTwitter
        streamingTwitter()

if __name__ == '__main__':

    #This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True                                                     # new code
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    streamingTwitter()
import tweepy
import sys

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

client = tweepy.Client(consumer_key=consumer_key, 
                       consumer_secret =consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret
                       )

def tweet(text):
    client.create_tweet(text=text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py 'text to tweet'")
        sys.exit(1)
    print("Tweet created!")
    tweet_text = sys.argv[1]
    tweet(tweet_text)



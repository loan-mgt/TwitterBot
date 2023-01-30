import tweepy
import requests
import Key

# Authenticate to Twitter
#auth = tweepy.OAuthHandler("KEY", "SECRET_KEY")
#auth.set_access_token("TOKEN", "SECRET_TOKEN")
auth = tweepy.OAuthHandler(Key.tweet_key, Key.tweet_secrete)
auth.set_access_token(Key.tweet_token, Key.tweet_token_secrete)

# Create API object
api = tweepy.API(auth)

def tweet(img,msg):
	
	r = requests.get(img, allow_redirects=True)
	with open('tmp.png', 'wb') as f:
		f.write(r.content)
	media_id = api.media_upload(filename='tmp.png')
	#api.update_status(status=msg,media_ids=[media_id] )

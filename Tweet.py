import tweepy
import requests

# Authenticate to Twitter
auth = tweepy.OAuthHandler("KEY", "SECRET_KEY")
auth.set_access_token("TOKEN", "SECRET_TOKEN")

# Create API object
api = tweepy.API(auth)

def tweet(img,msg):
	
	r = requests.get(img, allow_redirects=True)
	open('tmp.png', 'wb').write(r.content)
	api.update_with_media(filename='tmp.png',status=msg)

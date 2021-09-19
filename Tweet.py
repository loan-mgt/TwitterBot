import tweepy
import requests

# Authenticate to Twitter
auth = tweepy.OAuthHandler("R06IXvoGk7rcId2FOhWGyrWT7", "C0wzHSo2wfMrNGNXn25TMpyW9XpcZMAPSiVDEhO7pnxK7Cqk24")
auth.set_access_token("1308495726238986240-BFXTtzrnIip8SRBjgP5Tq2SV0SpAMt", "XEl7h7jJK7woDLcp24VEfhmfBCVilvmUt1OTFGvP9GKUq")

# Create API object
api = tweepy.API(auth)

def tweet(img,msg):
	
	r = requests.get(img, allow_redirects=True)
	open('tmp.png', 'wb').write(r.content)
	api.update_with_media(filename='tmp.png',status=msg)
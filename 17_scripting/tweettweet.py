import tweepy

auth = tweepy.OAuthHandler('hNyZJz9UIFhG5JbY95mG8Nd12', 'i7JnqGkHWc51nUM9B1EMH6WBKygOBNi8X4oWIV55aDJW1R1r5k')
auth.set_access_token('1375498024655351808-18onHEb0KNUOwyfVnGKjtPgAnugd43', 'llLErezUSIfDhWVpSOjjnMPu1rYXU2ZtzbFlvl1cWnPNE')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)
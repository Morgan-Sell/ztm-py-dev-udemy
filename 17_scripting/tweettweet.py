import tweepy

auth = tweepy.OAuthHandler("26ybcLaKlAZuHvtk48Y35si97", "jEOcunagAwM83WH8sElJfO1tQEeKKvBQRaR3zgX2637V5SdGJ")
#auth.set_access_token("AAAAAAAAAAAAAAAAAAAAAObKOAEAAAAAW21CNZma2kD9k%2B35", "Mz%2BFN0jsG14%3Dud4gmZa6X9TcwVx3vGWp9KUw9ma2lj2v1LKhohGPGpQHxfPCtY")

api = tweepy.API(auth)

# Bearer token
#api = "AAAAAAAAAAAAAAAAAAAAAObKOAEAAAAAW21CNZma2kD9k%2B35Mz%2BFN0jsG14%3Dud4gmZa6X9TcwVx3vGWp9KUw9ma2lj2v1LKhohGPGpQHxfPCtY"


public_tweets = api.home_timelie()
for tweet in public_tweets:
	print(tweet.text)
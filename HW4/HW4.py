import tweepy

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

with open('recent_tweets.txt','w',encoding='utf-8') as f:
	for tweet in public_tweets:
		date = tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
		content = tweet.text
		user = tweet.user.name
		location = tweet.user.location
		print('date: %s' % (date))
		print('user: %s' % (user))
		print('location: %s' % (location))
		print('content: %s' % (content))
		print('\n')
		f.write('date: %s' % (date))
		f.write('\n')
		f.write('user: %s' % (user))
		f.write('\n')
		f.write('location: %s' % (location))
		f.write('\n')
		f.write('content: %s' % (content))
		f.write('\n\n')
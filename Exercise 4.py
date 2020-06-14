import tweepy
consumer_key ='enter'
consumer_secret ='enter'
access_token ='enter'
access_token_secret ='enter'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
enter_url='https://twitter.com/KMbappe'
#enter_url=input('please enter twitter url')
enter_url=enter_url.split('/')
user=api.get_user(enter_url[len(enter_url)-1])
print('follower of @',user.screen_name,'is',user.followers_count)
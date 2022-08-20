import tweepy
import keys


client = tweepy.Client(keys.bearer_token(), keys.api_key(), keys.api_key_secret(), keys.access_token(), keys.accsess_token_secret())

auth = tweepy.OAuth1UserHandler(keys.api_key(), keys.api_key_secret(), keys.access_token(), keys.accsess_token_secret())
api = tweepy.API(auth)


person = client.get_user(username="PokiTono").data.id

for tweet in client.get_users_tweets(person).data:
   print(tweet.text)
print(get_users_tweets(person).data[0].id)
#client.create_tweet(in_reply_to_tweet_id=client.get_users_tweets(person).data[0].id, text="w")
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import tweepy
import random
import pandas as pd

# Twitter API credentials
key_df = pd.read_csv('twitter_api_keys.csv')
consumer_api_key = key_df[key_df.type == 'key']['Password'].values[0]
consumer_secret_key = key_df[key_df.type == 'secret']['Password'].values[0]
consumer_token = key_df[key_df.type == 'token']['Password'].values[0]
access_token_secret = key_df[key_df.type == 'access_token_secret']['Password'].values[0]
access_token = key_df[key_df.type == 'access_token']['Password'].values[0]

auth = tweepy.OAuthHandler(consumer_api_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# %%
retweeters = api.retweeters('TWEET ID')


# %%
entries = []

for i in retweeters:
	entries.append(api.get_user(i).screen_name)


# %%
if len(entries) == len(retweeters):
  # Chnage the number from 2 to how ever many random samples you'd like
	winners = random.sample(entries, 2)
	print("the winners of the giveaway are "+winners[0]+"and "+winners[1])
else:
	print("something went wrong")

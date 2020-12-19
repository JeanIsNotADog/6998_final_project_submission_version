import tweepy
import json
import random


'''
add twitter api credential data
'''
CONSUMER_KEY = 'xxxx'
CONSUMER_SECRET = 'xxxx'
OUTPUT_FILE = 'Results/Election20/08-18'
# tweet_ids = ['756453818855002112', '756453819651858432', '756453820943794180']

'''
import tweets_id and randomly sample 100 ids to look up
'''
df = pd.read_csv("TweetIDs/Election20/2020-08/08-18.txt", '\n', header=None)
ids_list = df.T.values.tolist()[0]
ids_list_100 = random.sample(ids_list, 100)



'''
make tweepy lookup call
'''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)
tweets = api.statuses_lookup(id_=ids_list_100, include_entities=False, trim_user=True)

tweets_json = []
for tw in tweets:
	tweets_json.append(tw._json)

with open(OUTPUT_FILE + '.json', 'w') as f:
	json.dump(tweets_json, f)




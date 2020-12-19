import yaml
import pandas as pd
import random
import json
from searchtweets import load_credentials, gen_rule_payload, collect_results
import numpy as np

# config = dict(
#     search_tweets_api = dict(
#         account_type = 'premium',
#         endpoint = 'https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json',
#         consumer_key = 'xxx',
#         consumer_secret = 'xxx',
#         bearer_token = 'xxxxxx'
#     )
# )


# with open('twitter_dev_creds.yaml', 'w') as config_file:
#     yaml.dump(config, config_file, default_flow_style=False)

OUTPUT_FILE_NAME = 'Results/Covid_CA/11-26'

# #######################  V2  ########################
# tags_rows = pd.read_csv("election_hashtags.csv", header=None).values.tolist()
# tags = []
# for row in tags_rows:
# 	tags.append(random.choice(row))

# tag_comb = ""
# for tag in tags:
# 	tag_comb += " OR " + "#" + tag

# tag_comb = tag_comb[len(" OR "):]
# QUERY_KEY=tag_comb
# #######################    ########################

# #######################  V3  ########################

QUERY_KEY=""
HH = str(random.choice(np.arange(8, 24)))
MM = str(random.choice(np.arange(60)))
if len(HH) == 1:
	HH = '0' + HH
if len(MM) == 1:
	MM = '0' + MM

# #######################   ########################

HH = '15'
MM = '30'

premium_search_args = load_credentials("twitter_dev_creds.yaml", yaml_key="search_tweets_api", env_overwrite=False)

rule = gen_rule_payload('(Covid OR COVID OR Coronavirus) lang:en place_country:CA', from_date='2020-11-25', to_date='2020-11-26 '+HH+':'+MM, results_per_call=100)
tweet = collect_results(rule, max_results=100, result_stream_args=premium_search_args)

with open(OUTPUT_FILE_NAME + '.json', 'w') as f:
	json.dump(tweet, f)


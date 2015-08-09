"""
run:
    $ python3 -m scripts.fetch.fetch_tweets
"""
from scripts.settings import congress_twitter_names, STALE_SECONDS
from scripts.settings import setup_space, get_twitter_api_from_creds
from scripts.settings import FETCHED_TWEETS_DIR
from scripts.utils.twitter import fetch_user_timeline
import json
from os.path import exists, getmtime, join
from time import time


if __name__ == '__main__':
    setup_space()
    api = get_twitter_api_from_creds()
    for screen_name in congress_twitter_names():
        fname = join(FETCHED_TWEETS_DIR, screen_name + '.json')
        # fetch tweets if file was not created more than 10 hrs ago
        if not exists(fname) or (time() - getmtime(fname)) > STALE_SECONDS:
            print("Fetching tweets for:", screen_name)
            tweets = fetch_user_timeline(api, screen_name)
            with open(fname, 'w') as f:
                print('Writing', fname)
                json.dump(tweets, f, indent = 2)

"""
run:
    $ python3 -m scripts.compile.compile_tweets

expects: ./stash/fetched/tweets has JSON files each containing a list of tweets

creates: ./stash/compiled/tweets/SCREENNAME.json for each fetched JSON
"""
from scripts.settings import FETCHED_TWEETS_DIR
from scripts.settings import COMPILED_TWEETS_DIR
from scripts.utils.extracts import TWEET_FIELDS, extract_tweet
from glob import glob
from os.path import join, basename, splitext
from os import makedirs
import json
import csv

if __name__ == '__main__':
    makedirs(COMPILED_TWEETS_DIR, exist_ok = True)
    for fn in glob(join(FETCHED_TWEETS_DIR, '*.json')):
        screen_name = splitext(basename(fn))[0]
        oname = join(COMPILED_TWEETS_DIR, screen_name + '.csv')
        tweets = json.load(open(fn))
        with open(oname, 'w') as o:
            print("Writing:", oname)
            # as a convenience, we add the tweet's author's screen_name
            #  which is not returned as part of the API
            c = csv.DictWriter(o, fieldnames = (['user_screen_name'] +  TWEET_FIELDS))
            c.writeheader()
            for tweet in tweets:
                t = extract_tweet(tweet)
                t['user_screen_name'] = screen_name
                c.writerow(t)


"""
run:
    $ python3 -m scripts.compile.compile_tweets

expects: ./stash/fetched/tweets has JSON files each containing a list of tweets

creates: ./stash/compiled/tweets/SCREENNAME.json for each fetched JSON
"""
from scripts.settings import setup_space
from scripts.settings import FETCHED_TWEETS_DIR
from scripts.settings import COMPILED_TWEETS_DIR
from scripts.utils.extracts import TWEET_FIELDS, extract_tweet
from glob import glob
from os.path import join, basename, splitext
import json
import csv

def munge_tweets_file(fn):
    """
    fn is a filename
    """
    for t in json.load(open(fn)):
        tweet = extract_tweet(t)
        tweet['user_screen_name'] = screen_name
        yield tweet

if __name__ == '__main__':
    setup_space()
    for fn in glob(join(FETCHED_TWEETS_DIR, '*.json')):
        screen_name = splitext(basename(fn))[0]
        oname = join(COMPILED_TWEETS_DIR, screen_name + '.csv')
        with open(oname, 'w') as o:
            print("Writing:", oname)
            # as a convenience, we add the tweet's author's screen_name
            #  which is not returned as part of the API
            c = csv.DictWriter(o, fieldnames = (['user_screen_name'] +  TWEET_FIELDS))
            c.writeheader()
            for tweet in munge_tweets_file(fn):
                c.writerow(tweet)


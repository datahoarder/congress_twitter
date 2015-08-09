import json
import os
import csv
from glob import glob

DATA_DIR = "./stash/"
FETCHED_DIR = os.path.join(DATA_DIR, "fetched")
FETCHED_CONGRESS_PROFILES_DIR = os.path.join(FETCHED_DIR, 'profiles')
FETCHED_TWEETS_DIR = os.path.join(FETCHED_DIR, 'tweets')
FETCHED_FRIENDS_IDS_DIR = os.path.join(FETCHED_DIR, 'friends_ids')
FETCHED_FRIENDS_PROFILES_DIR = os.path.join(FETCHED_DIR, 'friends_profiles')

COMPILED_DIR = os.path.join(DATA_DIR, "compiled")
TOP_FRIENDS_IDS_PATH = os.path.join(COMPILED_DIR, 'top-friends-ids.txt')

COMPILED_CONGRESS_PROFILES_PATH = os.path.join(COMPILED_DIR, 'congress-profiles.csv')
COMPILED_TOP_FRIENDS_PROFILES_PATH = os.path.join(COMPILED_DIR, 'top-friends-profiles.csv')
COMPILED_TOP_FRIENDSHIPS_PATH = os.path.join(COMPILED_DIR, 'top-friendships.csv')
COMPILED_TWEETS_DIR = os.path.join(COMPILED_DIR, 'tweets')

### packages stuff
PACKAGED_DIR = os.path.join(DATA_DIR, "packaged")
## meta data
SCHEMAS_DIR = "./meta/schemas"

TWITTER_CREDS_PATH = "./creds.json"

STALE_SECONDS = 3600 * 24 # 1 day
MIN_FRIEND_OCCURENCES = 10

def setup_space():
    os.makedirs(FETCHED_CONGRESS_PROFILES_DIR, exist_ok = True)
    os.makedirs(FETCHED_TWEETS_DIR, exist_ok = True)
    os.makedirs(FETCHED_FRIENDS_IDS_DIR, exist_ok = True)
    os.makedirs(FETCHED_FRIENDS_PROFILES_DIR, exist_ok = True)
    os.makedirs(COMPILED_TWEETS_DIR, exist_ok = True)
    os.makedirs(PACKAGED_DIR, exist_ok = True)

def get_twitter_api_from_creds(path = TWITTER_CREDS_PATH):
    from scripts.utils.twitter import get_api
    cpath = os.path.expanduser(path)
    creds = json.load(open(cpath))
    return get_api(creds['access_token'],
            creds['access_token_secret'],
            creds['consumer_key'],
            creds['consumer_secret'])

def congress_social_accounts():
    # why is there an ancillary directory? Should this
    # do its own fetch of the data? meh, rethink it later
    fn = os.path.join(DATA_DIR, 'ancillary', 'social-media-accounts.csv')
    return list(csv.DictReader(open(fn)))

def congress_twitter_names():
    return [d['twitter_username'].lower() for d in congress_social_accounts() if d['twitter_username']]

def congress_twitter_ids():
    return [d['twitter_id'] for d in congress_social_accounts() if d['twitter_id']]


def friends_ids_files():
    return glob(os.path.join(FETCHED_FRIENDS_IDS_DIR, '*.txt'))

import json
import os

DATA_DIR = "./stash/"
FETCHED_DIR = os.path.join(DATA_DIR, "fetched")
COMPILED_DIR = os.path.join(DATA_DIR, "compiled")
PACKAGED_DIR = os.path.join(DATA_DIR, "packaged")
## meta data
SCHEMAS_DIR = "./meta/schemas"

TWITTER_CREDS_PATH = "./creds.json"

def setup_space():
    os.makedirs(FETCHED_DIR, exist_ok = True)
    os.makedirs(COMPILED_DIR, exist_ok = True)
    os.makedirs(PACKAGED_DIR, exist_ok = True)


def get_twitter_api_from_creds(path = TWITTER_CREDS_PATH):
    from scripts.utils.twitter import get_api
    cpath = os.path.expanduser(path)
    creds = json.load(open(cpath))
    return get_api(creds['access_token'],
            creds['access_token_secret'],
            creds['consumer_key'],
            creds['consumer_secret'])

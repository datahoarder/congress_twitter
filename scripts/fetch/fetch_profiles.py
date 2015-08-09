"""
run:
    $ python3 -m scripts.fetch.fetch_profiles
"""
from scripts.settings import congress_twitter_names
from scripts.settings import setup_space, get_twitter_api_from_creds
from scripts.settings import FETCHED_CONGRESS_PROFILES_DIR
from scripts.utils.twitter import fetch_profiles
import json
import os.path



if __name__ == '__main__':
    setup_space()
    api = get_twitter_api_from_creds()
    for p in fetch_profiles(api, screen_names = congress_twitter_names()):
        sn = p['screen_name'].lower()
        fname = os.path.join(FETCHED_CONGRESS_PROFILES_DIR, sn + '.json')
        with open(fname, 'w') as f:
            print('Writing', fname)
            json.dump(p, f, indent = 2)

"""
run:
    $ python3 -m scripts.fetch.fetch_friends_profiles

expects that scripts/compile/compile_top_friends_ids.py has run
  and generated TOP_FRIENDS_IDS_PATH

creates: in FETCHED_FRIENDS_PROFILES_DIR, a JSON file for each friend ID number
"""
from scripts.settings import setup_space, get_twitter_api_from_creds
from scripts.settings import FETCHED_FRIENDS_PROFILES_DIR, TOP_FRIENDS_IDS_PATH
from scripts.utils.twitter import fetch_profiles
import json
import os.path

def run():
    setup_space()
    f_ids = open(TOP_FRIENDS_IDS_PATH).readlines()
    api = get_twitter_api_from_creds()
    for profile in fetch_profiles(api, user_ids = f_ids):
        # note that we fetch profile id from each retrieved profile
        p_id = str(profile['id'])
        p_sn = profile['screen_name']
        fname = os.path.join(FETCHED_FRIENDS_PROFILES_DIR, p_id + '.json')
        with open(fname, 'w') as f:
            print('Writing (%s): %s' % (p_sn, fname))
            json.dump(profile, f, indent = 2)



if __name__ == '__main__':
    run()

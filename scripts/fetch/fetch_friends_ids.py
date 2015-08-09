"""
run:
    $ python3 -m scripts.fetch.fetch_friends_ids
"""
from scripts.settings import congress_twitter_names
from scripts.settings import setup_space, get_twitter_api_from_creds
from scripts.settings import FETCHED_FRIENDS_IDS_DIR, STALE_SECONDS
from scripts.utils.twitter import fetch_friends_ids
from os.path import exists, getmtime, join
from time import time


if __name__ == '__main__':
    setup_space()
    api = get_twitter_api_from_creds()
    for screen_name in congress_twitter_names():
        fname = join(FETCHED_FRIENDS_IDS_DIR, screen_name + '.txt')
        # fetch tweets if file was not created more than 10 hrs ago
        if not exists(fname) or (time() - getmtime(fname)) > STALE_SECONDS:
            print("Fetching friends ids for:", screen_name)
            fids = fetch_friends_ids(api, screen_name)
            with open(fname, 'w') as f:
                for i in fids:
                    f.write(str(i) + "\n")

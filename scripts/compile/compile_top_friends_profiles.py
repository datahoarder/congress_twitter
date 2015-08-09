"""
run:
    $ python3 -m scripts.compile.compile_top_friends_profiles

expects: FETCHED_FRIENDS_PROFILES_DIR has JSON files for each Twitter profile

creates: COMPILED_TOP_FRIENDS_PROFILES_PATH
"""
from scripts.settings import FETCHED_FRIENDS_PROFILES_DIR
from scripts.settings import COMPILED_TOP_FRIENDS_PROFILES_PATH
from scripts.utils.extracts import TWITTER_PROFILE_FIELDS, extract_twitter_profile
from glob import glob
from os.path import join
import json
import csv

if __name__ == '__main__':
    c = csv.DictWriter(open(COMPILED_TOP_FRIENDS_PROFILES_PATH, 'w'),
                        fieldnames = TWITTER_PROFILE_FIELDS)
    c.writeheader()
    for fn in glob(join(FETCHED_FRIENDS_PROFILES_DIR, '*.json')):
        p = json.load(open(fn))
        pdata = extract_twitter_profile(p)
        c.writerow(pdata)


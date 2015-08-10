"""
run:
    $ python3 -m scripts.compile.compile_congress_profiles

expects: ./stash/fetched/profiles has JSON files for each Twitter profile

creates: ./stash/compiled/congress-profiles.csv
"""
from scripts.settings import FETCHED_CONGRESS_PROFILES_DIR
from scripts.settings import COMPILED_CONGRESS_PROFILES_PATH
from scripts.utils.extracts import TWITTER_PROFILE_FIELDS, extract_twitter_profile
from glob import glob
from os.path import join
import json
import csv


def run():
    c = csv.DictWriter(open(COMPILED_CONGRESS_PROFILES_PATH, 'w'),
                        fieldnames = TWITTER_PROFILE_FIELDS)
    c.writeheader()
    for fn in glob(join(FETCHED_CONGRESS_PROFILES_DIR, '*.json')):
        p = json.load(open(fn))
        pdata = extract_twitter_profile(p)
        c.writerow(pdata)


if __name__ == '__main__':
    run()

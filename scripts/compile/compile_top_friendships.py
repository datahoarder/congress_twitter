"""
run:
    $ python3 -m scripts.compile.compile_top_friendships

expects: TOP_FRIENDS_IDS_PATH to exist and
     friends_ids_files() has txt files

For every entry in TOP_FRIENDS_IDS_PATH, filters each txt file to just have
  top friends

creates: COMPILED_TOP_FRIENDSHIPS_PATH
"""
from scripts.settings import TOP_FRIENDS_IDS_PATH, FETCHED_FRIENDS_IDS_DIR
from scripts.settings import friends_ids_files
from scripts.settings import COMPILED_TOP_FRIENDSHIPS_PATH
from glob import glob
from os.path import basename, join, splitext
import csv

if __name__ == '__main__':
    c = csv.writer(open(COMPILED_TOP_FRIENDSHIPS_PATH, 'w'))
    c.writerow(['user_screen_name', 'friend_id'])
    all_top_ids = set([k.strip() for k in open(TOP_FRIENDS_IDS_PATH).readlines()])
    for fn in friends_ids_files():
        # get the user screen_name from the filename (icky)
        user_screen_name = splitext(basename(fn))[0]
        with open(fn) as f:
            _ids = set([k.strip() for k in f.readlines()])
            # filter ids for ids that are in all_top_ids
            top_friends_ids = all_top_ids.intersection(_ids)
            for t_id in top_friends_ids:
                c.writerow([user_screen_name, t_id])

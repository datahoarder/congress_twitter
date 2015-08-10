"""
run:
    $ python3 -m scripts.compile.compile_top_friends_ids

expects: friends_ids_files() has txt files

Reads every friend_ids and filters list for ids that occur
  more than scripts.settings.MIN_FRIEND_OCCURENCES
  And also includes every friend_id in scripts.settings.congress_twitter_ids
   regardless of occurrence (so that we can calculate most/least followed member)

creates: TOP_FRIENDS_IDS_PATH
"""

from scripts.settings import MIN_FRIEND_OCCURENCES
from scripts.settings import friends_ids_files
from scripts.settings import TOP_FRIENDS_IDS_PATH
from scripts.settings import congress_twitter_ids
from glob import glob
from collections import Counter
from os.path import join

def run():
    c = Counter()
    for fn in friends_ids_files():
        with open(fn) as f:
            c.update(k.strip() for k in f.readlines())
    top_ids = [str(f_id) for f_id, f_count in c.most_common() if f_count >= MIN_FRIEND_OCCURENCES]
    # now merge top_ids with congress_twitter_ids()
    cong_ids = [str(cid) for cid in congress_twitter_ids()]
    all_ids = list(set(top_ids + cong_ids))
    with open(TOP_FRIENDS_IDS_PATH, 'w') as o:
        o.write("\n".join(all_ids))

if __name__ == '__main__':
    run()

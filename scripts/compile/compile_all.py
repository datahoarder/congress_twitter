"""
A convenience script to run all the scripts in correct order

run:
    $ python3 -m scripts.compile.compile_all
"""


from scripts.compile import compile_congress_profiles
from scripts.compile import compile_top_friends_ids
from scripts.compile import compile_top_friends_profiles
from scripts.compile import compile_top_friendships
from scripts.compile import compile_tweets

def run():
    print("Compiling congress twitter profiles")
    compile_congress_profiles.run()
    print("Compiling congress tweets")
    compile_tweets.run()
    print("Filter and create the list of top friend ids")
    compile_top_friends_ids.run()
    print("Compile top friends' profiles")
    compile_top_friends_profiles.run()
    print("Create the top friendships file")
    compile_top_friendships.run()


if __name__ == "__main__":
    run()



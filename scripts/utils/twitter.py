# Helpful functions for accessing Twitter
import tweepy
TWITTER_PROFILE_BATCH_SIZE = 100
from math import ceil
from datetime import datetime


def get_api(access_token, access_token_secret, consumer_key, consumer_secret):
    """
    Takes care of the Twitter OAuth authentication process and
    creates an API-handler to execute commands on Twitter

    Arguments: string values

    Optional: if path is not None, it is expected to be a path to a JSON

    Returns:
      A tweepy.api.API object
    """
    # Get authentication token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # create an API handler
    return tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

def fetch_profiles(api, screen_names = [], user_ids = []):
    """
    A wrapper method around tweepy.API.lookup_users that handles the batch lookup of
      screen_names.

    `api` is a tweepy.API handle
    `screen_names` is a list of twitter screen names

    yields: a dict representing a Twitter profile

    https://dev.twitter.com/rest/reference/get/users/lookup
    """
    key, lookups = ['user_ids', user_ids] if user_ids else ['screen_names', screen_names]
    for batch_idx in range(ceil(len(lookups) / TWITTER_PROFILE_BATCH_SIZE)):
        offset = batch_idx * TWITTER_PROFILE_BATCH_SIZE
        # break lookups list into batches of TWITTER_PROFILE_BATCH_SIZE
        batch = lookups[offset:(offset + TWITTER_PROFILE_BATCH_SIZE)]
        try:
            for user in api.lookup_users(**{key: batch}):
                j = user._json
                yield j
        # except tweepy.RateLimitError:
        #     print("Rate limit error, sleeping")
        #     sleep(60 * 5) # five minutes
        # catch situation in which none of the names in the batch are found
        # or else Tweepy will error out
        except tweepy.error.TweepError as e:
            if e.response.status_code == 404:
                pass
            else: # some other error, raise the exception
                raise e


def fetch_user_timeline(api, screen_name, batch_limit = 0):
    """
    api is a tweepy.API object
    screen_name is a user's screen name, e.g. "GoStanford"
    batches is number of requests (at 200 tweets each) to make. 0 means maximum

    returns all tweets as an array
    """
    tweets = []
    cursor = tweepy.Cursor(api.user_timeline, screen_name = screen_name,
      trim_user = True, exclude_replies = False, include_rts = True, count = 200)
    pcursor = cursor.pages(batch_limit)
    while True:
        try:
            page = pcursor.next()
            for tweet in page:
                tweets.append(tweet._json)
        except StopIteration:
            break
    return tweets



def fetch_friends_ids(api, screen_name):
    ids = []
    cursor = tweepy.Cursor(api.friends_ids, screen_name = screen_name)
    pcursor = cursor.pages()
    while True:
        try:
            page = pcursor.next()
            ids.extend(page)
        except StopIteration:
            break
    return ids


def convert_timestamp(t):
    """
    t is something like 'Sat Jan 30 03:36:19 +0000 2010'
    return: a datetime object
    """

    return datetime.fromtimestamp(time.mktime(time.strptime(t, '%a %b %d %H:%M:%S +0000 %Y')))

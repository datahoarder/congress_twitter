import re

TWITTER_PROFILE_FIELDS = ["id", "name", "screen_name", "location",
    "description", "url", "followers_count", "friends_count", "listed_count",
    "created_at", "favourites_count", "statuses_count", "utc_offset", "time_zone",
    "verified", "geo_enabled", "lang", "profile_image_url",
    "profile_background_image_url", "profile_background_color", "profile_link_color"]

TWEET_FIELDS = ["id", "user_id", "source", "created_at",
    "retweet_count", "favorite_count", "text",
    "in_reply_to_screen_name", "in_reply_to_status_id",
    "retweeted_status_id", "retweeted_status_user_id", "retweeted_status_user_screen_name"]

def extract_twitter_profile(obj):
    """
    obj is a dict representing a Twitter user profile as returned by the API

    returns: a dict with filtered attributes
    """
    return {att: obj[att] for att in TWITTER_PROFILE_FIELDS}



def extract_tweet(t):
    """
    t is a dict representing a Twitter tweet as returned by the API

    returns: a dict for the tweet with filtered attributes
    """
    d = {}
    rt = t.get('retweeted_status')
    for f in TWEET_FIELDS:
        if f == 'user_id':
            d['user_id'] = t['user']['id']
        elif f == 'source':
            x = re.search(r'(?<=>).+?(?=<\/a>)', t['source'])
            d['source'] = x.group() if x else t['source']
        elif f == 'text':
            d['text'] = re.sub("\s+", ' ', t['text']).strip()
        elif f == 'retweeted_status_id':
            d['retweeted_status_id'] = rt['id'] if rt else None
        elif f == 'retweeted_status_user_id':
            d['retweeted_status_user_id'] = rt['user']['id'] if rt else None
        elif f == 'retweeted_status_user_screen_name':
            # note that the screen_name of retweeted user is extracted from
            # the tweet's text
            d['retweeted_status_user_screen_name'] = (
                re.search(r'(?<=^RT @)\w+(?=:)', t['text']).group()) if rt else None
        else:
            d[f] = t[f]
    return d

"""
run:
    $ python3 -m scripts.fetch.fetch_profiles
"""
from scripts.settings import setup_space
from scripts.settings import FETCHED_DIR
from utils.twitter import fetch_profiles, get_api
import os.path
import requests

if __name__ == '__main__':
    setup_space()

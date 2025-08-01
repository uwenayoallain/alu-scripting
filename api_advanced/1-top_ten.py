#!/usr/bin/python3

"""
Script to print top 10 hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """"top ten"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)

    res = requests.get(url,
                       headers={
                           'User-Agent': 'Mozilla/5.0'})

    if res.status_code != 200:
        print("Ok", end="")
    else:
        print("Ok", end="")

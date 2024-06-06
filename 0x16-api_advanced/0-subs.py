#!/usr/bin/python3
"""The Script Does the Following:
 + Queries the Reddit API
 + Returns the number of subscribers for a given subreddit.
 + Not active users, total subscribers
 + If an invalid subreddit is given, the function should return 0. 
"""

import requests

def number_of_subscribers(subreddit):
    """Takes a subreddit and returns the number of subscribers """
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(f'http://www.reddit.com/r/{subreddit}/about.json',
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs

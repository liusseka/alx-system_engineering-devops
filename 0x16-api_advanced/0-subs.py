#!/usr/bin/python3
"""
The script queries a subreddit api for subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()

        if data.get("kind") == "t5":
            return data["data"]["subscribers"]
        else:
            return 0

    except requests.exceptions.RequestException:
        return 0

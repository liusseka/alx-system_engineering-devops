#!/usr/bin/python3
"""The Script Does the Following:
 + Queries the Reddit API
 + Returns the number of subscribers for a given subreddit.
 + Not active users, total subscribers
 + If an invalid subreddit is given, the function should return 0. 
"""

import requests

def number_of_subscribers(subreddit):
	"""Returns number of subcribers"""
	if subreddit is None or type(subreddit) if not str:
		return 0

	url = f'https://www.reddit.com/r/{subreddit}/about.json'
	headers = {
	"User-Agent": "SubredditSubscriberCounter/1.0"
	}

	try:
		res = requests.get(url, headers=headers, allow_redirects=False)
		data = res.json()
		return data['data']['subscribers']

	except requests.exceptions.RequestException:
		return 0

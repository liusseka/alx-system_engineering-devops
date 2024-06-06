#!/usr/bin/python3
"""
The Script that Queries a Reddit API
"""

import requests

def number_of_subscribers(subreddit):
	"""
	Returns number of subcribers

	Args:
	   takes a subreddit title

	Returns:
	   Number of Subscribers
	"""
	if subreddit is None or type(subreddit) if not str:
		return 0

	url = f'https://www.reddit.com/r/{subreddit}/about.json'
	headers = {
	"User-Agent": "SubredditSubscriberCounter/v.1.0"
	}

	try:
		res = requests.get(url, headers=headers, allow_redirects=False)
		data = res.json()
		return data['data']['subscribers']

	except requests.exceptions.RequestException:
		return 0

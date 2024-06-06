#!/usr/bin/python3
"""The Script that Queries a Reddit API"""

import requests

def number_of_subscribers(subreddit):
	"""Returns number of subcribers"""
	if subreddit is None or type(subreddit) if not str:
		return 0

	url = f'https://www.reddit.com/r/{subreddit}/about.json'
	headers = {
	"User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/Julius_Charles"
	}

	try:
		res = requests.get(url, headers=headers, allow_redirects=False)
		data = res.json()
		return data['data']['subscribers']

	except requests.exceptions.RequestException:
		return 0

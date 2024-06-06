#!/usr/bin/python3
"""The Script Does the Following:
 + Queries the Reddit API
 + Returns the number of subscribers for a given subreddit.
 + Returns 0 If an invalid subreddit is given. 
"""

import requests

def number_of_subscribers(subreddit):
	"""Returns number of subcribers"""
	if subreddit is None or type(subreddit) if not str:
		return 0

	# defines url and parameters
	url = f'https://www.reddit.com/r/{subreddit}/about.json'
	headers = {
	"User-Agent": "SubredditSubscriberCounter/1.0"
	}

	# Requests and returns the data
	try:
		res = requests.get(url, headers=headers, allow_redirects=False)
		data = res.json()
		return data['data']['subscribers']

	except requests.exceptions.RequestException:
		return 0

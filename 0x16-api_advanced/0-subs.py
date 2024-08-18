#!/usr/bin/python3

"""Returns number of subscribers"""

import requests

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API for the subscriber count of a subreddit.

  Args:
      subreddit (str): The name of the subreddit to query.

  Returns:
      int: The number of subscribers for the subreddit, or 0 if invalid.
  """
  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {'User-Agent': 'My Reddit API Script 1.0'} 

  try:
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status()

    data = response.json()
    return data.get('data', {}).get('subscribers', 0)
  except requests.exceptions.RequestException:
    return 0  # Return 0 on any request error

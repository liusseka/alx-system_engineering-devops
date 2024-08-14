import requests

def top_ten(subreddit):
  """
  This function queries the Reddit API for the titles of the top 10 hot posts in a subreddit.

  Args:
      subreddit (str): The name of the subreddit to query.
  """
  url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10" 
  headers = {'User-Agent': 'My Reddit API Script 1.0'} 

  try:
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status() 

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
      print(None) 
      return

    for post in posts:
      title = post['data'].get('title')
      if title:
        print(title)

  except requests.exceptions.RequestException:
    print(None) 
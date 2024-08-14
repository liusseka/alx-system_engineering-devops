import requests

def recurse(subreddit, hot_list=[], after=None):
  """
  This function recursively retrieves titles of all hot articles for a subreddit.

  Args:
      subreddit (str): The name of the subreddit to query.
      hot_list (list, optional): Accumulates titles across recursive calls. Defaults to [].
      after (str, optional): The "after" parameter for pagination. Defaults to None.

  Returns:
      list: A list of all hot article titles, or None if invalid subreddit.
  """
  url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100" 
  if after:
    url += f"&after={after}"
  headers = {'User-Agent': 'My Reddit API Script 1.0'}

  try:
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status() 

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
      return hot_list 

    for post in posts:
      title = post['data'].get('title')
      if title:
        hot_list.append(title)

    after = data.get('data', {}).get('after') 

    # Recursive call with "after" parameter for next page
    return recurse(subreddit, hot_list, after)

  except requests.exceptions.RequestException:
    return None
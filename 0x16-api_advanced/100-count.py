#!/usr/bin/python3
"""
Module for a function that queries the Reddit API recursively.
"""

import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """
    Queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    
    - Keywords are case-insensitive and delimited by spaces.
    - "Javascript" should count as "javascript", but "java" should not.
    - If no posts match or the subreddit is invalid, it prints nothing.
    """
    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_dict:
            if count > 0:
                print(f'{word}: {count}')
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json()['data']
        posts = data['children']
        after = data['after']

        for post in posts:
            title_words = post['data']['title'].lower().split()
            for word in word_dict:
                word_dict[word] += title_words.count(word)

    except (KeyError, ValueError):
        return

    count_words(subreddit, word_list, after, word_dict)
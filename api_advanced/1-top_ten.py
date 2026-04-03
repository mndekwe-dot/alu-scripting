#!/usr/bin/python3
"""Module that queries the Reddit API and prints top 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Query Reddit API and print titles of first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    params = {"limit": 10}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)

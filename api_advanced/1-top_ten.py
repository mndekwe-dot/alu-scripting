#!/usr/bin/python3
"""Module to query Reddit API and print top 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced.project:v1.0 (by /u/student)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    if not posts:
        print(None)
        return
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))

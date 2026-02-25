#!/usr/bin/python3
"""Module to query Reddit API for subscriber count of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)

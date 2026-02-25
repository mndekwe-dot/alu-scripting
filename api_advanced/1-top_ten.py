#!/usr/bin/python3
"""Module to query Reddit API and print top 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Prints None if the subreddit is invalid or not found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0)"
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            params={"limit": 10}
        )
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return
        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            print(title)
    except Exception:
        print(None)

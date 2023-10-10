#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the top 10 hotest posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        data = response.json()["data"]
        count = 1
        for post in data["children"]:
            if count <= 10:
                print(count, post["data"]["title"])
            count += 1
        return 0
    except Exception as e:
        print("None", e)

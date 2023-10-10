#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Prints a sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as
    javascript, but java should not).
    """
    keywords = word_list.split(" ")

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    if after:
        headers["after"] = after
        url = f"{url}?after={after}"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()["data"]
            after = data.get("after", None)
            for post in data["children"]:
                title = post["data"]["title"]
                hot_list.append(title)
                for word in str(title).split(" "):
                    if word in keywords:
                        # + here
            if after:
                count_words(subreddit, word_list, hot_list, after)
                return host_list
        except Exception as e:
            print("--E--:", e)
            return None
    else:
        return None

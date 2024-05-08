#!/usr/bin/python3
"""returns the number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                      "Mobile Safari/537.36"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    elif response.status_code != 200:
        print(f"API request failed with status code {response.status_code}")
        return None

    try:
        data = response.json().get("data")
        return data.get("subscribers")
    except ValueError:
        print("Invalid JSON format in the response")
        return None

# Example usage:
subreddit_name = "programming"
subscribers_count = number_of_subscribers(subreddit_name)
if subscribers_count is not None:
    print(f"Subscribers in r/{subreddit_name}: {subscribers_count}")
else:
    print("Error occurred while fetching subscribers.")

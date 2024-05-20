#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv

def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    try:
        response = requests.get(url, headers=user)
        response.raise_for_status()
        data = response.json()
        hot_posts = data['data']['children']
        if hot_posts:
            for post in hot_posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.exceptions.HTTPError:
        print(None)
    except (KeyError, json.decoder.JSONDecodeError):
        print(None)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(argv[1])

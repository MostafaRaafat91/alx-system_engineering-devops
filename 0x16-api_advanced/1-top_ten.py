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
        if not hot_posts:
            print(f"No posts found for subreddit '{subreddit}'")
        else:
            for post in hot_posts:
                print(post['data']['title'])
    except requests.exceptions.HTTPError:
        print(f"Error: Unable to fetch data for subreddit '{subreddit}'")
    except KeyError:
        print(f"Error: No posts found for subreddit '{subreddit}'")
    except json.decoder.JSONDecodeError:
        print(f"Error: Unable to decode JSON response from Reddit API for subreddit '{subreddit}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python 1-main.py <subreddit>")
    else:
        top_ten(argv[1])

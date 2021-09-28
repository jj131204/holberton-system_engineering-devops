#!/usr/bin/python3
""" ... """


import requests


def top_ten(subreddit):
    """ ... """

    url = ('https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit))
    head = {"User-Agent": "jj131204"}
    test = requests.get(url, headers=head).json()

    if test.get('error') == 404:
        print('None')

    else:
         data = test.get('data').get('children')
         for i, obj in enumerate(data):
             if i == 11:
                 break
             print(obj.get('data').get('title'))

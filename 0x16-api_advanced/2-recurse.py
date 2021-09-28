#!/usr/bin/python3
""" ... """


import requests


def recurse(subreddit, hot_list=[], after=None):
    """ ... """

    if not after:
        url = 'https://www.reddit.com/r/{}/hot.json?'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'\
            .format(subreddit, after)
    head = {"User-Agent": "jj131204"}
    test = requests.get(url, headers=head).json()

    if test.get('error') == 404:
        print('None')

    else:
        data = test.get('data').get('children')
        for obj in data:
            hot_list.append(obj.get('data').get('title'))
        after = test.get('data').get('after')
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)

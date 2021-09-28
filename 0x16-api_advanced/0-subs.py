#!/usr/bin/python3
""" ... """


import requests


def number_of_subscribers(subreddit):
    """ ... """

    url = ('https://www.reddit.com/r/{}/about.json'.format(subreddit))
    head = {"User-Agent": "jj131204"}
    test = requests.get(url, headers=head).json()

    if test.get('error') == 404:
        return 0
    else:
        return test.get('data').get('subscribers')

import requests
import json
from pprint import pprint
from time import time


def get_comments(url, n=400):
    headers = {'User-agent': 'creative writing downloader'}
    params = {'limit': n}
    url = url + '.json'
    res = requests.get(url, headers=headers, params=params)
    data = json.loads(res.text)
    comments = data[1]['data']['children']
    result = list()
    for comment in comments:
        try:
            result.append(comment['data']['body'])
        except Exception as oops:
            a = oops
    return result


def get_top_posts():
    url = 'https://www.reddit.com/r/WritingPrompts/top/.json?t=month'
    headers = {'User-agent': 'creative writing downloader'}
    params = {'limit': 400}
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        return res.json()
    else:
        print('error', res.json())
        return None


posts = get_top_posts()
for post in posts['data']['children']:
    comments = get_comments('https://www.reddit.com' + post['data']['permalink'])
    print('# comments:', len(comments), 'link:', post['data']['permalink'])
    for comment in comments:
        if 'I am a bot' in comment:
            continue
        if len(comment) < 300:
            continue
        with open('stories/story_%s.txt' % time(), 'w', encoding='utf-8') as outfile:
            outfile.write(comment)
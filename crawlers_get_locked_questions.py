"""
获取官网上的加锁题目
"""

import urllib.request
import json

url = "https://leetcode.com/api/problems/all/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url, headers=headers)
webURL = urllib.request.urlopen(req)
raw_data = json.loads(webURL.read())["stat_status_pairs"]
locked_questions = []

for item in raw_data:
    if item["paid_only"]:
        locked_question_info = {"id": item["stat"]["frontend_question_id"], "title": item["stat"]["question__title"]}
        locked_questions.append(locked_question_info)

print(len(locked_questions))





# -*- coding: utf-8 -*-
import  requests
import json
result = requests.get("https://api.weibo.com/2/statuses/home_timeline.json?access_token=2.00uQG_8C0QuSJn2d5a6a76c3q8fqmC",verify=False).content
#print result
result_json=json.loads(result)
statuses=result_json["statuses"]
statuses_json=json.loads(statuses)
# -*- coding: utf-8 -*-
import  requests
import time
import random
import logging
from multiprocessing import Pool


base_url="http://54.67.94.143:9092"
aff_id=1468
def fff(x):
    click_url = base_url + "/transaction/post_click?offer_id=85548&aff_id=" + str(aff_id) + "&aff_sub=SUB1&aff_sub2=SUB2&aff_sub3=SUB3&aff_sub4=SUB4&source=main_expite&aff_sub6=test"
    # 测试环境offer_id=5&aff_id=7，线上环境offer_id=317&aff_id=129
    click_res = requests.post(click_url, allow_redirects=False).content  # 发起点击
    print str(x)+'----'+click_res
    return 0


if __name__ == '__main__':
    p = Pool(16)
    p.map(fff, range(16))


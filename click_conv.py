# -*- coding: utf-8 -*-
import  requests
import time
import random

#base_url="http://eu.atracking.appflood.com"
base_url="http://pre.service.aflt.papayamobile.com"
#base_url="http://54.215.117.231:1256"
#设置基地址
#aff_list = ["21", "883", "1416", "1420", "1459"]
aff_list=["1435","1482","1458","1429","1400","1032","1481","700","25","1457","1452"]

def click_conv(index,aff_id):

    click_url = base_url+"/transaction/post_click?offer_id=112544&aff_id="+aff_id+"&aff_sub=SUB1&aff_sub2=SUB2&aff_sub3=SUB3&aff_sub4=SUB4&aff_sub5=SUB5&source=deduct&aff_sub6=testtime"+str(index)
    #测试环境offer_id=5&aff_id=7，线上环境offer_id=317&aff_id=129
    click_res = requests.post(click_url,allow_redirects=False).content#发起点击
    print click_res
    #time.sleep(1)
    position=click_res.index("transaction_id")
    tran_id= click_res[position+15:position+49]#截取transactionID
    print tran_id
    conv_url=base_url+"/transaction/post_conversion?transaction_id="+tran_id
    print conv_url
    conv_res=requests.post(conv_url,allow_redirects=False).content#确认转化

    print conv_res
    if conv_res =='"1"':
        print 'conversion ok'
    #time.sleep(1)
    event_url=base_url+"/transaction/event?transaction_id="+tran_id+"&name=eventtest&value=8"
    event_res=requests.post(event_url,allow_redirects=False).content#产生事件
    print event_res


for i in range(100):#设置循环次数

    aff_id=aff_list[random.randint(0,10)]
    print '第%d次请求' % (i + 1)
    #print "aff_id:" + aff_id

    click_conv(i,aff_id)


# -*- coding: utf-8 -*-
import  requests
import time

#base_url="http://eu.atracking.appflood.com"
base_url="http://pre.service.aflt.papayamobile.com"
#base_url="http://54.215.117.231:1256"
#设置基地址

def click_conv(index):
    click_url = base_url+"/transaction/post_click?offer_id=5&aff_id=6&aff_sub=SUB1&aff_sub2=SUB2&aff_sub3=SUB3&aff_sub4=SUB4&aff_sub5=SUB5&source=SRC&aff_sub6=testtime"+str(index)
    #测试环境offer_id=5&aff_id=7，线上环境offer_id=317&aff_id=129
    click_res = requests.post(click_url,allow_redirects=False).content#发起点击
    print click_res
    time.sleep(1)
    position=click_res.index("transaction_id")
    tran_id= click_res[position+15:position+49]#截取transactionID
    print tran_id
    conv_url=base_url+"/transaction/post_conversion?transaction_id="+tran_id
    print conv_url
    conv_res=requests.post(conv_url,allow_redirects=False).content#确认转化

    print conv_res
    if conv_res =='"1"':
        print 'conversion ok'
    time.sleep(1)
    event_url=base_url+"/transaction/event?transaction_id="+tran_id+"&name=eventtest&value=8"
    event_res=requests.post(event_url,allow_redirects=False).content#产生事件
    print event_res


for i in range(10):#设置循环次数
    print '第%d次请求'%(i+1)
    click_conv(i)


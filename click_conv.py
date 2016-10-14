# -*- coding: utf-8 -*-
import  requests
import time
import random
import logging
from multiprocessing import Pool
logging.basicConfig(
                format='%(asctime)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='click_convertion.log',
                filemode='a')

#base_url="http://auto.atracking.appflood.com"
base_url="http://pre.service.aflt.papayamobile.com"
#base_url="http://54.67.94.143:9092"#dynamic测试地址
#base_url="http://54.215.117.231:1256"
#设置基地址
#aff_list = ["21", "883", "1416", "1420", "1459"]
#aff_list=["1435","1482","1458","1429","1400","1032","1481","700","25","1457","1452"]
aff_list=["1500","1501","1502","1503","1504","1505","1506"]#pre
#aff_list=["1458","1468"]#test

current_time=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
print current_time
def click_conv(index):
    print '第%03d次请求' % (index + 1)
    sub_str=str("%03d"%(index+1))
    aff_id = aff_list[random.randint(0, len(aff_list)) - 1]
    click_url = base_url+"/transaction/post_click?offer_id=151979&aff_id="+aff_id+"&aff_sub=SUB1&aff_sub2=SUB2&aff_sub3=SUB3&aff_sub4=SUB4&source=batch_create&aff_sub6=test"+sub_str+"&aff_sub5="+current_time
    print click_url
    #测试环境offer_id=5&aff_id=7，线上环境offer_id=317&aff_id=129
    click_res = requests.post(click_url,allow_redirects=False).content#发起点击
    print click_res
    time.sleep(2)
    position=click_res.find("transaction_id")
    if position==-1:
        print ("click failed,cannot find transaction_id!")
        logging.warning(sub_str+'\t'+aff_id+'\t'+"no transaction_id")
        return -1

    tran_id= click_res[position+15:position+49]#截取transactionID
    print tran_id
    conv_url=base_url+"/transaction/post_conversion?transaction_id="+tran_id
    #print conv_url
    conv_res=requests.post(conv_url,allow_redirects=False).content#确认转化

    print conv_res
    if conv_res =='"1"':
        print 'conversion ok'
    #time.sleep(1)
    event_url=base_url+"/transaction/event?transaction_id="+tran_id+"&name=eventtest&value=8"
    event_res=requests.post(event_url,allow_redirects=False).content#产生事件
    #print event_res
    log_text=sub_str+'\t'+aff_id+'\t'+tran_id#记录日志
    logging.warning(log_text)
    return 1

logging.warning('mission start')
# for i in range(10):#设置循环次数
#     print '第%03d次请求' % (i + 1)
#     click_conv(i)
    #log_text= "aff_id:" + aff_id
    #logging.debug('log_text')
    #print ("%03d"%(i+1))
if __name__ == '__main__':
    p = Pool(6)
    print(p.map(click_conv, range(6)))
logging.warning('mission complete')


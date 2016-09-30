# -*- coding: utf-8 -*-
import  requests
import time
#测cap用，和click_conv的区别是，这个程序先做完所有的click，再去发conversion
#base_url="http://atracking.appflood.com"
#base_url="http://pre.service.aflt.papayamobile.com"
#base_url="http://54.215.117.231:1256"
base_url="http://54.67.94.143:9092"
#设置基地址
def do_click(index):
    click_url = base_url + "/transaction/post_click?offer_id=85483&aff_id=1458&aff_sub=SUB1&aff_sub2=SUB2&aff_sub3=SUB3&aff_sub4=SUB4&aff_sub5=l&aff_sub6=testtime" + str(index)
    # 测试环境offer_id=5&aff_id=7，线上环境offer_id=317&aff_id=129
    click_res = requests.post(click_url, allow_redirects=False).content  # 发起点击
    print click_res
    time.sleep(1)
    position = click_res.index("transaction_id")
    tran_id = click_res[position + 15:position + 49]  # 截取transactionID
    return tran_id

def do_convertion(tran_id):
    conv_url = base_url + "/transaction/post_conversion?transaction_id=" + tran_id
    print conv_url
    conv_res = requests.post(conv_url, allow_redirects=False).content  # 确认转化
    print conv_res
    if conv_res == '"1"':
        print 'conversion ok'
    time.sleep(1)

transaction_id=[]
for i in range(10):
    #do_click(i)
    transaction_id.append(do_click(i))
for j in range(10):
    do_convertion(transaction_id[j])

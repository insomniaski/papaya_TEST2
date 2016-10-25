# -*- coding: utf-8 -*-
import  requests
import time
#用于线上多节点测试
base_url="technologyaffiliate.com"
node_list=["","usw.","sg.","jp.","sa.","eu.","au.","in.","auto."]#八个节点的域名前缀，没前缀的是美东，auto是自动
url_list=[]
for i in range(9):
    url_list.append("http://"+node_list[i]+base_url)#初始化8个节点的url
#print url_list

def click_conv(node_url,node_info):   #对节点发送一组三个tracking
    click_url = node_url+"/transaction/post_click?offer_id=203984&aff_id=128&aff_sub=SUB1&aff_sub2=SUB2&aff_sub3=SUB3&aff_sub4=SUB4&aff_sub5=SUB5&source=SRC&aff_sub6=Testnode:"+node_info
    #测试环境offer_id=5&aff_id=7，线上环境offer_id=317&aff_id=129
    click_res = requests.post(click_url,allow_redirects=False).content#发起点击
    print click_res
    time.sleep(1)
    position=click_res.index("transaction_id")
    tran_id= click_res[position+15:position+49]#截取transactionID
    print tran_id
    conv_url=node_url+"/transaction/post_conversion?transaction_id="+tran_id
    print conv_url
    conv_res=requests.post(conv_url,allow_redirects=False).content#确认转化

    print conv_res
    if conv_res =='"1"':
        print 'conversion ok'
    time.sleep(1)
    event_url=node_url+"/transaction/event?transaction_id="+tran_id+"&name=eventtest&value=8"
    event_res=requests.post(event_url,allow_redirects=False).content#产生事件
    print event_res

for j in range(9):
    print "测试节点："+node_list[j]
    click_conv(url_list[j],node_list[j])


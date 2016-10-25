# -*- coding: utf-8 -*-
import requests
import logging
class appfloodrequest:
    base_url=""
    environment=""
    transaction_id=""
    aff_id=""
    offer_id=""
    sub1=""
    sub2=""
    sub3=""
    sub4=""
    sub5=""
    sub6=""
    source=""

    def __init__(self,env,aff_id,offer_id):
        if (env=='pre'):
            self.base_url="http://pre.service.aflt.papayamobile.com"
        elif(env=='test'):
            self.base_url="http://54.215.117.231:1256"
        elif(env=='master'):
            self.base_url="http://auto.atracking.appflood.com"
        else:
            print "please set environment!"
            return 0
        self.aff_id=aff_id
        self.offer_id=offer_id

        print ("appflood request initialized")

    def click(self):
        click_url=self.base_url+"/transaction/post_click"
        data = {
            'offer_id':self.offer_id,
            'aff_id':self.aff_id,
            'source': self.source,
            'sub1': self.sub1,
            'sub2': self.sub2,
            'sub3': self.sub3,
            'sub4': self.sub4,
            'sub5': self.sub5,
            'sub6': self.sub6,
        }
        click_res = requests.post(click_url,data=data,allow_redirects=False).content
        #print click_url
        print click_res
        position = click_res.find("transaction_id")
        if position == -1:
            print ("click failed,cannot find transaction_id!")
            #logging.warning(sub_str + '\t' + aff_id + '\t' + "no transaction_id")
            return -1
        else:
            self.transaction_id = click_res[position + 15:position + 49]#获取transaction_id


requests1=appfloodrequest('pre',1458,5)
requests1.click()
print requests1.transaction_id
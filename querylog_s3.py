# -*- coding: utf-8 -*-

#用于生产s3的查询语句

path ="/var/log/fluentd/s3/s3."
log_type=["","test_","pre_"]
log_name=["click_cb_log","revenue_payout_cb_log","revenue_payout_kernel_log"]
log_prefix="appflood_affiliate_daily_"
log_valid=["invalid_","valid_"]

def gene_query(a,b,c):
    return path+log_type[a]+log_prefix+log_valid[b]+log_name[c]

print "querylog "+'"cat '+gene_query(0,1,0)+'/*t"'

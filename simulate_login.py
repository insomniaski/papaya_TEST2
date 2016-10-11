# -*- coding: utf-8 -*-
import  requests
base_url="http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com/postLogin"
data={
    'email':'wangyiqian@papayamobile.cn',
    'password':'5c6442062bca20e7eccec0e2bde9149af22c0587f0b8682aade3c5966f7716d7',
    'auth':'admin',
}
print requests.post(base_url,data=data).content
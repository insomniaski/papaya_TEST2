# -*- coding: utf-8 -*-
import paramiko

hostname='52.78.59.221'
port=22
username='dev'
pkey="D:\papaya\precn2.pem"
key=paramiko.RSAKey.from_private_key_file(pkey)
s=paramiko.SSHClient()
#s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(hostname,port,username,pkey=key)
stdin,stdout,stderr=s.exec_command('ssh fluentd-viewer-usw')
print stdout.read()
stdin,stdout,stderr=s.exec_command('ssh fluentd-3')
print stdout.read()
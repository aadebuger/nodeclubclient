# -*- coding: utf-8 -*-
'''
Created on 2017年9月2日

@author: aadebuger
'''
import requests
import pymongo

def topics():
    url="https://cnodejs.org/api/v1"+"/topics"
    ret=requests.get(url)
    print("text",ret.text)
def newtopic():
    url="https://cnodejs.org/api/v1"+"/topics"
    ret=requests.post(url,data={'accesstoken':"b29c5ff3-a1bb-4f3b-8709-17da9ee6fd98","title":"hello","tab":"dev","content":"hello"})
    print("text",ret.text)
def newtopiclocal(cat):
    url="http://localhost:3000/api/v1"+"/topics"
    ret=requests.post(url,data={'accesstoken':"f45459ad-30eb-41c1-b8cd-a4341a27f66b","title":"hello","tab":cat,"content":"hello"})
    print("text",ret.text)
def signup():
    url="http://localhost:3000/signup"
    formdata={"loginname":"test2","pass":"test2","re_pass":"test2","email":"test2@qq.com"}
    ret = requests.post(url,data=formdata)
    print("text",ret.text)
def updateActive(accesstoken):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.node_club_dev
    db.users.find({})
    db.users.update({'accessToken':accesstoken},{'$set':{'active':true}})

if __name__ == '__main__':
    topics()
#    newtopic()
    newtopiclocal("ask")
    
    signup()
    
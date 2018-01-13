# -*- coding:utf-8 -*-
import random
import time
n = 0
m = 0
t1 = time.time()
print u'数据乘法练习--2位和3位数乘以1位数'

#-------------------
# log_dump
#-------------------
def log_dump(filename,content):
    fpath = filename
    f = file(fpath,'ab')
    t_s = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    fs = f.write(t_s + '->' + str(content) + '\r\n')
    f.close()
    return 
    

log_dump('log.txt','---------------------------------------------------------------')    
while True:

    i = random.randint(11,999)
    j = random.randint(5,9)

    print '-------------',u'对的次数:',n,u' 错误的次数:',m, u' 时间(秒):',int(time.time()-t1)
    print i,'x',j,''
    try:
    
        s = raw_input('=')
        k = int(s)
        if i * j == k:
            log_dump('log.txt','right, i=%d,j=%d,k=%d' %(i,j,k))
            print u'对!'
            n += 1
        else:
            log_dump('log.txt','wrong, i=%d,j=%d,k=%d' %(i,j,k))        
            print u'错'
            m += 1
    except:
        pass
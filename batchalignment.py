'''
Created on 2014-3-25

@author: gndy
'''
import os
import sys
'''
python调用muscle进行批量比对，读取一个目录下的所有fas文件，依次传到muscle参数中，进行比对。
'''
faslist = os.listdir(sys.argv[1])
i = 0
for file in faslist:
    #print 'muscle -in %s -out %s -maxiters 2'%(sys.argv[1]+'/'+file,sys.argv[1]+'/output/'+file+'aligned')
    os.system('muscle -in %s -out %s'%(sys.argv[1]+'/'+file,sys.argv[2]+file+'.aligned'))
    i = i+1
    print i

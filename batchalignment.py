'''
Created on 2014-3-25

@author: gndy
'''
import os
import sys
'''
python����muscle���������ȶԣ���ȡһ��Ŀ¼�µ�����fas�ļ������δ���muscle�����У����бȶԡ�
'''
faslist = os.listdir(sys.argv[1])
i = 0
for file in faslist:
    #print 'muscle -in %s -out %s -maxiters 2'%(sys.argv[1]+'/'+file,sys.argv[1]+'/output/'+file+'aligned')
    os.system('muscle -in %s -out %s'%(sys.argv[1]+'/'+file,sys.argv[2]+file+'.aligned'))
    i = i+1
    print i

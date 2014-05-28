#coding:utf-8
'''
Created on 2014-5-27

@author: gndy
'''

import os,sys,re
#比较两个目录中的文件
list_1 = os.listdir(sys.argv[1])
list_2 = os.listdir(sys.argv[2])

for i in range(len(list_1)):
    file_1 = open(sys.argv[1]+list_1[i]).readlines()#逐行比较
    file_2 = open(sys.argv[2]+list_2[i]).readlines()
    for ii in range(len(file_1)):
        words_1 = file_1[ii].split('\t')[0:-1]
        words_2 = file_2[ii].split('\t')[0:-1]
        myset = set()#用集合来合并相同的氨基酸分布
        digitlist_1 = []#文件1的数字list
        digitlist_2 = []#文件2的数字list
        aalist_1 = []#文件1的氨基酸list
        aalist_2 = []#文件2的氨基酸list
        for word in words_1:
            digitlist_1.append(word[0:-1].strip())
            aalist_1.append(word[-1])
            myset.add(word[-1])
        for word in words_2:
            digitlist_2.append(word[0:-1].strip())
            aalist_2.append(word[-1])
            myset.add(word[-1])
        print ','.join(myset)
        #print digitlist_1
        #print aalist_1
        #print digitlist_2
        #print aalist_2
        resultdigitlist_1 = []
        resultdigitlist_2 = []
        
        for i in myset:
            if i in aalist_1:
                tmp_1 = re.sub('^[0-9]{1,3}\s+','',digitlist_1[aalist_1.index(i)])#正则替换掉行号和空格
                resultdigitlist_1.append(tmp_1)#统计所有的氨基酸分布
            else:
                resultdigitlist_1.append('0') #没有的就用0来补齐
        print ','.join(resultdigitlist_1)  
        
        for i in myset:
            if i in aalist_2:
                tmp_2 = re.sub('^[0-9]{1,3}\s+','',digitlist_2[aalist_2.index(i)])
                resultdigitlist_2.append(tmp_2)
            else:
                resultdigitlist_2.append('0') 
        print ','.join(resultdigitlist_2)             
             

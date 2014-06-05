#coding:utf-8
import sys,os
'''
给序列文件加上fasta头，会替换掉原来的文件，注意备份（惨剧啊！- -）
'''
files = os.listdir(sys.argv[1])

for file in files:
    fasta_head = '>'+file.split('.')[0]+'_consensus\n'
    oldFile = open(sys.argv[1]+file)
    old_content = oldFile.readline()
    new_content = fasta_head+old_content
    newFile = open(sys.argv[1]+file,'w')
    newFile.write(new_content)
    
    
    

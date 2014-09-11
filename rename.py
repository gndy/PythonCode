#coding:utf-8
import os,sys

for filename in os.listdir(sys.argv[1]):
    #print file
    old = sys.argv[1]+filename
    #print old
    new = sys.argv[1]+filename.replace('.aligned','')
    #print new
    os.rename(old,new)

#coding:utf-8
import os,sys
'''
读取percentage文件，每次读取四个片段的序列文件（同一个目录下）。
每次读取需要手工输入四个片段的起始位置，依次与相应的consensus序列
进行比较，统计出突变率（这种形式：204,M,I,93.52，方便直接粘贴道excel）
'''
filenames = os.listdir(sys.argv[2])#含有序列文件的目录，只能含有四个片段的序列文件
filenames.sort()
bases = sys.argv[1].split(',')#每个文件序列片段的起始位置
consensus = open(sys.argv[3],'r').readline()#consensus序列的读取

for i in range(len(filenames)):
    print filenames[i]

    contents = open(sys.argv[2]+filenames[i],'r').readlines()
    base = int(bases[i])
    
    for content in contents:
        mutations = content.strip().split('\t')
        if len(mutations)>1:
            mutations.sort()
            tmp = []
            tmp1 = []
            for ii in mutations:
                if ii.split(',')[1] != consensus[base-1]:
                    tmp.append(ii.split(',')[1])
                    tmp1.append(str(float(ii.split(',')[0])*100))
            print str(base)+','+consensus[base-1]+','+'/'.join(tmp)+','+'/'.join(tmp1)
        base = base+1
    


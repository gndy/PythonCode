#coding:utf-8
import os,sys
'''
对hbv的四段consensus序列进行拼接，主要是判断头尾的氨基酸相同的位点，然后进行切片并连接
其中有些序列的头尾连4个相同的氨基酸都没有，而只有两个氨基酸相同，所以还需要手工来处理这些
序列
'''
files = os.listdir(sys.argv[1])
files.sort()
work_files = []
for i in range(len(files)):
    j = i%4
    work_files.append(sys.argv[1]+files[i])
    fasta_head = '>'+files[i].split('-')[0]+'consensus'
    if j == 3:
	my_consensus = []
	seg_1 = open(work_files[0]).readline()
	seg_2 = open(work_files[1]).readline()
	seg_3 = open(work_files[2]).readline()
	seg_4 = open(work_files[3]).readline()
	for ii in range(len(seg_1)):
	    if seg_1[ii] == seg_2[0] and seg_1[ii+1] ==seg_2[1] and seg_1[ii+2] == seg_2[2] and seg_1[ii+3] == seg_2[3]:
                my_consensus.append(seg_1[0:ii])
	for ii in range(len(seg_2)):
	    if seg_2[ii] == seg_3[0] and seg_2[ii+1] ==seg_3[1] and seg_2[ii+2] == seg_3[2] and seg_2[ii+3] == seg_3[3]:
                my_consensus.append(seg_2[0:ii])
	for ii in range(len(seg_3)):
	    if seg_3[ii] == seg_4[0] and seg_3[ii+1] ==seg_4[1] and seg_3[ii+2] == seg_4[2] and seg_3[ii+3] == seg_4[3]:
                my_consensus.append(seg_3[0:ii])
        my_consensus.append(seg_4)
        print fasta_head
        print ''.join(my_consensus)
        work_files = []


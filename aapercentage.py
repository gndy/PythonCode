#coding:utf-8

from cogent.core.profile import Profile
from cogent import LoadSeqs, PROTEIN 
import os,sys
'''
author:wenlei
获取蛋白比对序列每列的氨基酸分布比率
'''
def fileToFrequency(filePath):
	aln = LoadSeqs(filePath,moltype = PROTEIN)
	pf = aln.getPosFreqs()
	pf.normalizePositions()
	lines = pf.prettyPrint(include_header = True,col_sep=',').split('\n')#每行数据的列表
	header_line = lines[0].split(',')#头行数据列表

	str_tmp = ''
	for line in lines[1::]:

	    line_content = line.split(',')
	    for i in range(len(line_content)):
		if (float(line_content[i].strip()) > 0.01 and header_line[i].strip() != '-' and header_line[i].strip() != 'X'):#1是突变率的阈值，2是是否为-，3是是否为X
		   str_tmp = str_tmp+line_content[i]+','+header_line[i].strip()+'\t'
	    str_tmp = str_tmp +'\n'
	return str_tmp

files = os.listdir(sys.argv[1])
for file in files:
	filename = sys.argv[1]+file
	resultString = fileToFrequency(filename)
	open(sys.argv[2]+file+".percentage",'w').write(resultString)


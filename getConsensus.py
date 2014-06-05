#coding:utf-8

from cogent.core.profile import Profile
from cogent import LoadSeqs, PROTEIN 
import os,sys
'''
author:wenlei
获取consensus序列
'''
def fileToFrequency(filePath):
	aln = LoadSeqs(filePath,moltype = PROTEIN)
	pf = aln.getPosFreqs()
	str_tmp = pf.toConsensus(fully_degenerate=False)
	return str_tmp

files = os.listdir(sys.argv[1])
for file in files:
	filename = sys.argv[1]+file
	resultString = fileToFrequency(filename)
	open(sys.argv[2]+file+".fasta",'w').write(resultString)


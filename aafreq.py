from cogent.core.profile import Profile
from cogent import LoadSeqs, PROTEIN 
'''
author:wenlei
获取蛋白比对序列每列的氨基酸分布
'''
aln = LoadSeqs('./aa.fasta',moltype = PROTEIN)
pf = aln.getPosFreqs()
lines = pf.prettyPrint(include_header = True,col_sep=',').split('\n')#每行数据的列表
header_line = lines[0].split(',')#头行数据列表

count = 1
for line in lines[1::]:
    str_tmp = str(count)+' '
    count = count+1
    line_content = line.split(',')
    for i in range(len(line_content)):
        if line_content[i].strip() != '0':#判断是否为0
	   str_tmp = str_tmp + line_content[i]+header_line[i].strip()+'\t'
    print str_tmp



        



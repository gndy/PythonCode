from cogent.core.profile import Profile
from cogent import LoadSeqs, PROTEIN 
'''
author:wenlei
��ȡ���ױȶ�����ÿ�еİ�����ֲ�
'''
aln = LoadSeqs('./aa.fasta',moltype = PROTEIN)
pf = aln.getPosFreqs()
lines = pf.prettyPrint(include_header = True,col_sep=',').split('\n')#ÿ�����ݵ��б�
header_line = lines[0].split(',')#ͷ�������б�

count = 1
for line in lines[1::]:
    str_tmp = str(count)+' '
    count = count+1
    line_content = line.split(',')
    for i in range(len(line_content)):
        if line_content[i].strip() != '0':#�ж��Ƿ�Ϊ0
	   str_tmp = str_tmp + line_content[i]+header_line[i].strip()+'\t'
    print str_tmp



        



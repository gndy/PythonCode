#coding:utf-8
import xlrd

def getMean(list):
    if list == []:
        return 0.0
    l=len(list)
    m=float(sum(list))/l
    return m

data = xlrd.open_workbook('/home/wenlei/RT_MUTATION_MINE.xls')
table = data.sheets()[0]
values_all = {}
resistant_position = [80,84,85,153,169,173,180,181,184,191,194,202,204,207,214,215,236,250]
resistant_freq = []

for i in range(0,table.ncols,5):
    
    for ii in range(1,len(table.col_values(i))):
        value = table.col_values(i)[ii]#序号
        name = table.col_values(i+1)[0]
        value_2 = table.col_values(i+3)[ii]#突变率
        value_3 = 0#把多个突变率求和
        value_4 = str(table.col_values(i+1)[ii])#原氨基酸
        value_5 = str(table.col_values(i+2)[ii])#突变的氨基酸

        if '/' in str(value_2):
            for j in value_2.split('/'):
                value_3 = value_3+float(j)
        else:
            value_3 = value_2
        values_all[value] = str(value_3)
    if '' in values_all.keys():
        del values_all['']
    for aa in resistant_position:
        if aa in values_all.keys():
            resistant_freq.append(str(values_all[aa]))
            del values_all[aa]
	else:
	    resistant_freq.append('0')
    #print name+'\t'+str(getMean(resistant_freq))+'\t'+str(getMean(values_all.values()))[0:4]
    #下面是进行Mann-Whitney u test进行数据整理的部分，如果只需要平均值，可注释掉下面的部分，取消上面一句的注释
    my_values = values_all.values()
    for i in range(326-len(my_values)):
        my_values.append('0')
        
    
    print ','.join(resistant_freq)
    print ','.join(my_values)
    print '========================='
    
    values_all = {}
    resistant_freq = []


#coding:utf-8
import xlrd

'''
把突变率的变化趋势和标准差以及位点的数据整理成
<位点 00w ....78w 标准差> 的形式
如：<204	0	0.22	0.38	1.48	4.2	62.23	92.56	35.36>。
前半部分是算标准差的代码，我是直接用的其中部分结果，代码重复率很高，主要是
怕以后要用，所以都传上github，懒！
'''

def stdDeviation(a):#算标准差
        l=len(a)
        m=float(sum(a))/l
        d=0
        for i in a:
            d = d+(i-m)**2
        return (d/l)**0.5

data = xlrd.open_workbook('/home/wenlei/mutation_of_14_0-78w.xls')
table = data.sheets()[0]
values_all = []
for i in range(0,table.ncols,5):
    raw_list = [0 for k in range(345)]
    for ii in range(len(table.col_values(i))):
        value = table.col_values(i)[ii]#序号
        value_2 = table.col_values(i+3)[ii]#突变率
        value_3 = 0#把多个突变率求和
        value_4 = str(table.col_values(i+1)[ii])#原氨基酸
        value_5 = str(table.col_values(i+2)[ii])#突变的氨基酸

        if '/' in str(value_2):
            for j in value_2.split('/'):
                value_3 = value_3+float(j)
        else:
            value_3 = value_2
        if value != '':
            raw_list[int(value)] = value_3
    values_all.append(raw_list)
    
results = {}
content = open('/home/wenlei/SD_14_0-78w_modified').readlines()#标准差的排序文件
num = [i.split(',')[0] for i in content]#位点的list
sd = [i.split(',')[1] for i in content]#标准差的list
j=0
for i in num:
    tmp = []
    for values in values_all:
        tmp.append(str(values[int(i)]))
    print 'A\t'+i+'\t'+'\t'.join(tmp)+'\t'+sd[j]
    j = j+1

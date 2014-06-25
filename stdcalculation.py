#coding:utf-8
import xlrd

'''
计算vbk病人中，各个采样时期突变率的标准差，找出
用药之后变异度最大的位点的排序
'''

def stdDeviation(a):#算标准差
        l=len(a)
        m=float(sum(a))/l
        d=0
        for i in a:
            d = d+(i-m)**2
        return (d/l)**0.5

data = xlrd.open_workbook('/home/wenlei/RT_MUTATION_MINE.xls')
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
for i in range(1,345):
    tmp = []
    for values in values_all:
        tmp.append(values[i])
    result = stdDeviation(tmp)
    results[result] = i
    
result_1 = sorted(results.iteritems(),key=lambda results:results[0],reverse=True)#对标准差的大小进行排序
for i in result_1:
    print str(i).strip('(').strip(')')

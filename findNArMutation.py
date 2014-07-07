#coding:utf-8
import xlrd
'''
找出和抗药相关位点的突变情况，打印出来
'''

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
        name = table.col_values(i+1)[0]#病人编号
        wild = table.col_values(i+1)[ii]#原aa
        mutation = table.col_values(i+2)[ii]#突变后的aa        
        rate = table.col_values(i+3)[ii]#突变率
        if value in resistant_position:
            print name+','+str(int(value))+','+wild+','+mutation+','+str(rate)

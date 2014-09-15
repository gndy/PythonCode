#coding:utf-8
import xlrd
import matplotlib.pyplot as plt

data = xlrd.open_workbook('/home/wenlei/S-gene-baseline-mutation.xls')
table = data.sheets()[0]


for i in range(0,table.ncols,5):
    name = table.col_values(i+1)[0]
    values_all = [0 for k in range(1,227)]
    for ii in range(len(table.col_values(i))):
        value_one = table.col_values(i)[ii]
        value_two = table.col_values(i+3)[ii]
        value_three = 0
        if '/' in str(value_two):
            for j in value_two.split('/'):
                value_three = value_three+float(j)
        else:
            value_three = value_two
        if value_one != '':
            values_all[int(value_one)] = value_three

    plt.plot(values_all)
    plt.title(name)
    plt.ylim(0,50)
    plt.xlabel('Position')
    plt.ylabel('Frequency')
    plt.savefig(name+'.png')
    plt.show()

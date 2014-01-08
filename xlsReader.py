'''
Created on 2013-12-31

@author: gndy
'''

import xlrd

data = xlrd.open_workbook("F6 barcode.xls")
table = data.sheets()[0]

strings = []

rows = table.nrows
for i in range(rows):
    
    if(table.cell(i,3).value!="" and table.cell(i,3).value!="blank"):
        for j in range(1,9):
            string = table.cell(i,3).value+table.cell(i+j,4).value.replace('se','')+'\t'+table.cell(i+j,5).value.replace(' ','')[25:]
            strings.append(string)
for i in strings:
    print i
#print len(strings)
print u'\xa0'
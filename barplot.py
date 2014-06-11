import xlrd
import matplotlib.pyplot as plt

data = xlrd.open_workbook('/home/wenlei/RT_MUTATION_MINE.xls')
table = data.sheets()[0]
values_all = []
for i in range(0,table.ncols,5):
    values_all.extend(table.col_values(i))
new_values = [x for x in values_all if x != '']
my_list = [0 for i in range(344)]
for i in new_values:
    my_list[int(i)] = my_list[int(i)]+1

xdata = [i for i in range(1,345)]
colors = []#color array
myX = []#X coordinates for texts
myY = []#Y coordinates for texts
myTexts = []# texts list
for i in range(len(my_list)):
    if my_list[i]>15:
	print i
        colors.append('r')
	myX.append(i)
	myY.append(my_list[i])
	myTexts.append(str(i))
    else:
        colors.append('b')
	myX.append(0)
	myY.append(0)
	myTexts.append('')
plt.bar(xdata,my_list,color=colors)
plt.title('Mutation sites statistic')
plt.xlabel('Position')
plt.ylabel('Frequency')
myX[124] = myX[124]-4#主要是一些微调用于使重叠的字符分开
myX[127] = myX[127]+1
myX[267] = myX[267]-5
myX[269] = myX[269]+2
for i in range(len(myX)):
    plt.text(myX[i],myY[i],myTexts[i],fontsize=13)
plt.show()

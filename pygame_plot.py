#coding:utf-8
# This is an example that uses pygame.draw.rect:
import os, sys
import random
import pygame
import xlrd
from pygame.locals import *

pygame.init()
APPLICATION_x_size = 1500
APPLICATION_y_size = 600
screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
pygame.display.set_caption('Fun Boring Example comes with Source Code too!!')

black_square_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
black_square_that_is_the_size_of_the_screen.fill((255, 255, 255))
screen.blit(black_square_that_is_the_size_of_the_screen, (0, 0))


def getSites():
    data = xlrd.open_workbook('/home/wenlei/RT_MUTATION_baseline.xls')
    table = data.sheets()[0]
    valuesAll = []
    for i in range(0,table.ncols,5):
        single_list = [0 for a in range(344)]
        name = table.col_values(i+1)[0]
        nums = [int(j) for j in table.col_values(i) if j != '']
        freqs = [sumFreqs(j) for j in table.col_values(i+3) if j != '']
        for k in range(len(nums)):
            single_list[nums[k]] = freqs[k]
        single_list[0] = name    
        valuesAll.append(single_list)
    return valuesAll

def sumFreqs(freq_strs):
    if "/" in str(freq_strs):
        return sum([float(i) for i in freq_strs.split("/") ])
    return float(freq_strs)
        
        
def myDraw(x,y,sites):
    for i in range(1,len(sites)):
        childX = x+i*3
        childY = y
        Mycolor = colorSelect(sites[i])
        pygame.draw.rect(screen , Mycolor , (childX, childY,   3,   20))
        
def colorSelect(value):
    first_color = (255,211,199)
    second_color = (207,138,138)
    third_color = (157,78,78)
    forth_color = (106,30,30)
    fivth_color = (63,8,8)
    WHITE_WHITE_HOORAY = (255, 255, 255)
    
    if value<1 and value>0:
        return WHITE_WHITE_HOORAY
    elif value>1 and value<10:
        return second_color
    elif value>10 and value<30:
        return third_color
    elif value>30 and value<50:
        return forth_color
    elif value>50:
        return fivth_color
    else:
        return WHITE_WHITE_HOORAY
        
        
        
myfont = pygame.font.SysFont("monospace", 15)#设置字体  

sites = getSites()
responders = [sites[q] for q in[0,1,5,6,7,10,11,12,13,17,20,21,23,25]]
partial_res = [sites[w] for w in [4,8,15,18,19,22,24]]
vbk = [sites[e] for e in [2,9,14,16,24]]

for site in sites:
    ccc=0
    for item1 in range(1,len(site)):
        if int(site[item1])>=1:
            ccc+=1
    print site[0]
    print ccc

Y = 1
for i in responders:
    myDraw(80,Y,i)
    name = i[0]
    label = myfont.render(name, 1, (0,0,0))
    screen.blit(label, (0, Y))#画文字
    Y = Y+20
    
for i in partial_res:
    myDraw(80,Y,i)
    name = i[0]
    label = myfont.render(name, 1, (0,0,0))
    screen.blit(label, (0, Y))#画文字
    Y = Y+20
    
for i in vbk:
    myDraw(80,Y,i)
    name = i[0]
    label = myfont.render(name, 1, (0,0,0))
    screen.blit(label, (0, Y))#画文字
    Y = Y+20
    
    
pygame.draw.line(screen,(0,0,0),(80,530),(1300,530))#画直线

for i in range(0,380,50):
    x = 80+i*3
    pygame.draw.rect(screen , (0,0,0) , (x, 525,   1,   6))#坐标轴刻度
    label = myfont.render(str(i), 1, (0,0,0))
    screen.blit(label, (x-6, 535))#坐标数字微调

first_color = (255,211,199)
second_color = (207,138,138)
third_color = (157,78,78)
forth_color = (106,30,30)
fivth_color = (63,8,8)    

pygame.draw.rect(screen , first_color , (1300, 423,   20,   25))#坐标轴刻度
pygame.draw.rect(screen , second_color , (1300, 450,   20,   25))#坐标轴刻度
pygame.draw.rect(screen , third_color , (1300, 477,   20,   25))#坐标轴刻度
pygame.draw.rect(screen , forth_color , (1300, 504,   20,   25))#坐标轴刻度
pygame.draw.rect(screen , fivth_color , (1300, 531,   20,   25))#坐标轴刻度

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    


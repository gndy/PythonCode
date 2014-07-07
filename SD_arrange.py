
# coding: utf-8



stds = open('./SD_24_0-78w_modified').readlines()

for i in stds:
    std = i.split(',')[0]
    position = i.split(',')[1].strip()
    point = std.index('.')
    print position+','+std[0:point+3].strip()








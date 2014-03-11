# -*- coding:utf-8 -*-
import sys
import urllib
import time
import os
from selenium import webdriver
def main():
    #获取参数
    url=sys.argv[1]
    #操作IE
    driver=webdriver.Firefox()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #创建目录
    
   
    dir_name='/home/wenlei/pics'
    
    
    if(os.path.exists(dir_name)!=True):
        os.mkdir(dir_name)
    images=driver.find_elements_by_tag_name('img')
   
    for image in images:
        image_url=str(image.get_attribute('src'))
        img_file=urllib.urlopen(image_url)
        byte=img_file.read()
        print 'donwload complete!','-'*10,'size:',len(byte)/1024,'KB'
        if(byte.__len__()>7000):
            file_name=image_url.split('/')[-1]
            #file_name=file_name.replace(':','_')
            write_file=open(dir_name+'/'+file_name,'wb')
            write_file.write(byte)
            write_file.close()
            print dir_name+file_name,'complete!'
    driver.quit()
if __name__ == '__main__':
    main()

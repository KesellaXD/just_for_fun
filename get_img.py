# coding:utf-8
import urllib.request  
import re
import os
 
def getHtml(url):
    page = urllib.request.urlopen(url);
    html = page.read();
    return html;
 
def getImg(html):
    imglist = re.findall('img src="(http.*?)"',html)#1 #http.*?表示非贪婪模式的匹配，只要符合http就匹配完成，不再看后面的内容是否匹配，即在能使整个匹配成功的前提下，使用最少的重复
    return imglist
 
html = getHtml(r"https://passport.aicai.com/xpassport/aicai/login/index?redirectUrl=https://kaijiang.aicai.com/").decode("utf-8");
imagesUrl = getImg(html);
 
if os.path.exists("D:/imags") == False:
    os.mkdir("D:/imags");
     
count = 0; #文件的起始名称为 0
for url in imagesUrl:
    print(url)
    if(url.find('.') != -1):#2
        name = url[url.find('.',len(url) - 5):];
        bytes = urllib.request.urlopen(url);
        f = open("D:/imags/"+str(count)+name, 'wb');  #代开一个文件，准备以二进制写入文件
        f.write(bytes.read());#write并不是直接将数据写入文件，而是先写入内存中特定的缓冲区
        f.flush();#将缓冲区的数据立即写入缓冲区，并清空缓冲区
        f.close();#关闭文件
        count+=1;

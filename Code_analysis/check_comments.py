'''
Created on 31 Jul 2017

@author: Piotr Laskowski
'''

import urllib.request
from bs4 import BeautifulSoup,Comment
from builtins import str

print("*"*80)       
print("\t\t\tChecking comments")
print("*"*80) 

spider = open("E:\ETH\zap_spider.txt","r")
new_comments = open("E:\ETH\zap_spider_new.txt","a")
for line in spider:
   
    try:
        resource = urllib.request.urlopen(line)
        page_source = resource.read().decode("utf-8")
        soup = BeautifulSoup(page_source, 'html.parser')
        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
       
        if comments:
            print("*"*80)  
            print("\tURL: "+line, end='') #Source page URL
            print('\n[+] ', comments) #Actual comments
            print("\n"+"*"*80)
            

            value1 = "*"*20+"\n"
            value1 += "URL: "+line
            value1 += '\n[+] {}'.format(comments)
            value1 += "\n"+"*"*20+"\n"
            new_comments.write(str(value1))
            
           
    except:
        continue
new_comments.close()  
print("*"*20)       
print("Checking comments completed")
print("*"*20)
        
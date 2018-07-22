
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

os.chdir("C:\\Users\\morim\\OneDrive\\ドキュメント\\Python\\投資信託")



def returns():
    url= []
    url.append("https://www.nikkei.com/markets/fund/ranking/?type=returnup&term=1y")
    for i in range(2,6):
        url.append("https://www.nikkei.com/markets/fund/ranking/?type=returnup&term=1y&category1=&page={0}".format(i))
    
    names=[]
    returns=[]

    for i in range(0, len(url)):
        html= urlopen(url[i])
        data = html.read()
        html = data.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        name_ = soup.find_all("td", class_="left") 
        return_ = soup.find_all("td", class_="right a-fs14")
        for j in name_:
            a= j.find("a")
            names.append(a.text)
        for j in return_:
            returns.append(j.text)
    returns2=[]
    for k in range(0,300,3):
        returns2.append(returns[k])
    
    for l,m in zip(names, returns2):
        print("{0:40s}:{1}".format(l, m), "\n")



if __name__ == "__main__":
    returns()






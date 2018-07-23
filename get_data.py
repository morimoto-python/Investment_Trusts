
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
    
    for l,(m,n) in enumerate(zip(names, returns2)):
        print("{0}位:{1:40s} {2}".format(l+1, m, n), "\n")

def risks():
    url= []
    url.append("https://www.nikkei.com/markets/fund/ranking/?term=3y&type=risk")
    for i in range(2,6):
        url.append("https://www.nikkei.com/markets/fund/ranking/?category1=&page={0}&term=3y&type=risk".format(i))
    
    names=[]
    risks=[]

    for i in range(0, len(url)):
        html= urlopen(url[i])
        data = html.read()
        html = data.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        name_ = soup.find_all("td", class_="left") 
        risk_ = soup.find_all("td", class_="right a-fs14")
        for j in name_:
            a= j.find("a")
            names.append(a.text)
        for j in risk_:
            risks.append(j.text)
    risks2=[]
    for k in range(0,300,3):
        risks2.append(risks[k])
    
    for l,(m,n) in enumerate(zip(names, risks2)):
        print("{0}位:{1:40s} {2}".format(l+1, m, n), "\n")

if __name__ == "__main__":
    returns()
    risks()






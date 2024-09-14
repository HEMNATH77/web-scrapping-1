import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")

n = soup.find_all("a",class_="title")
a = []

for i in n:
    p_names = i.text
    a.append(p_names)
    #print(a)

p = soup.find_all("h4",class_="price float-end card-title pull-right")
d=[]

for i in p:
    p_price = i.text
    d.append(p_price)
    #print(d)

m = soup.find_all("p",class_="description card-text")
b=[]

for i in m:
    p_des = i.text
    b.append(p_des)
    #print(b)

o = soup.find_all("p",class_="review-count float-end")
c=[]

for i in o:
    p_rate = i.text
    c.append(p_rate)
    #print(c)

df = pd.DataFrame({"Product Name":a,"Prices":d,"Description":b,"Reviews":c})
#print(df)

df.to_csv("Product details.csv")





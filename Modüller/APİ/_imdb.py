import requests
import json
import os
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mp_mv250"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    span = tr.find("td",{"class":"titleColumn"}).find("span").text
    sort = (tr.td.titleColumn)
    print(sort,title, span)

# print(list)


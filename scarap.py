from bs4 import  BeautifulSoup 
from selenium import webdriver
import time 
import csv
import pandas as pd
start_url= "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser= webdriver.Chrome()
browser.get(start_url)
time.sleep(10)
stars_data=[]

Soup=BeautifulSoup(browser.page_source,"html")

star_table=Soup.find_all("table")
temp_list=[]
table_rows=star_table[7].find_all("tr")
for tr in table_rows :
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

stars=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(temp_list)):
    stars.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])
df=pd.DataFrame(list(zip(stars,distance,mass,radius)),columns=["star name","Distance","mass","radius"])
df.to_csv("info.csv")
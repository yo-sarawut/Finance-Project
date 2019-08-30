import os
import pandas as pd
from datetime import date
import pandas_datareader.data as web 
import numpy as np


f = open("temp.txt",encoding='utf-8')
r = f.readlines()
r.encodeing('ascii', 'ignore')
print(r[30:100])
f.close()


# +++++++++++++++++++++++++++++++++++++++

#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/04/2562&date2=05/04/2562"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify()) 

# +++++++++++++++++++++++++++++++++++++++++++++


import requests
url = 'http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/04/2562&date2=30/04/2562'
r = requests.get(url) 
data = r.text
data.encodeing = "ascii"
print(data[30:100])

import requests 
URL = "http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/04/2562&date2=30/04/2562"
r = requests.get(URL) 
r.encodeing('utf-8')
print(r.content[30:100]) 


f = open('temp.txt','w',encoding='utf-8')
f.write (str(data))
print(data[30:100])
f.close()

with open('temp.txt', encoding='utf-8') as f:
    for line in f:
        print(repr(line))


# Download + Write data to text file
import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/07/2562&date2=31/07/2562"
r = requests.get(URL)   
soup = BeautifulSoup(r.content, 'html5lib') 

soup =soup.find("body") 
print(soup.prettify()) 

data = soup.prettify()

print(len(data))

# write data to text file
f = open('temp.txt','w',encoding='utf-8')
f.write (str(data))
f.close()
print('success')

# ++++++++++++++++++++++++++++++++++++++++++

# Read text file + Clean data







# +++++++++++++++++++++++++++++++++++++++
# Master Source Code

#This will not run on online IDE 

import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/05/2562&date2=31/05/2562"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify()) 

# +++++++++++++++++++++++++++++++++++++++++++++

# v+++++++++++++++++++++++++++++++++++++++

import requests 
from bs4 import BeautifulSoup 
  
def news(): 
    # the target we want to open     
    url='http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/04/2562&date2=05/04/2562'
      
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        print("Successfully opened the web page") 
        print("The news are as follow :-\n") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     
  
        # l is the list which contains all the text i.e news  
        l=soup.find("body")
      
        #now we want to print only the text part of the anchor. 
        #find all the elements of a, i.e anchor 
        for i in l.findAll("pre"): 
            print(i.text) 
    else: 
        print("Error") 
          
news()
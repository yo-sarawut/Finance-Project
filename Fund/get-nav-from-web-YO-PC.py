

# Import ข้อมูลจาก Website ที่มีบริการให้ download NAV ย้อนหลังได้ครั้งละ 1 เดือน

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3



def read_nav(years, months):
    y = years
    m = months
    for i in range(len(months)):
        if months[i] == '02':
            URL = (
                f'http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/{months[i]}/{years}&date2=29/{months[i]}/{years}')
        else:
            URL = (
                f'http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/{months[i]}/{years}&date2=31/{months[i]}/{years}')
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        soup = soup.find("body")
        # print(soup.prettify())
        data = soup.prettify()
        print(len(data))

        # write data to text file
        f = open(f'NAV/NAV_{years}_{months[i]}.txt', 'w', encoding='utf-8')
        f.write(str(data))
        f.close()
        print(f'{years}_{months[i]}-success')
years = '2562'
months = ['06']
read_nav(years, months)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def read_txt(years, months):
    y = years
    m = months
    for i in (months):
        n = ['nav_date', 'B', 'C', 'Firm', 'E', 'proj_name_th', 'proj_name_en', 'fund_code', 'net_asset',
             'nav_price', 'dividend_value', 'book_close_date', 'sell_price', 'buy_price']
        df = pd.read_csv(
            (f'NAV/NAV_{years}_{months}.txt'), header=None, names=n, skiprows=1, encoding='utf-8')
        # ลบข้อมูลที่เป็น่ค่าว่าง
        df = df.dropna(subset=['fund_code'])

        # Convert Type to DateTime
        df['nav_date'] = pd.to_datetime(df.nav_date, dayfirst=True)
        df['book_close_date'] = pd.to_datetime(df.book_close_date, dayfirst=True)

        df = df.loc[:, ['nav_date', "fund_code", 'nav_price', 'net_asset', 'sell_price',
                        'buy_price', 'dividend_value', 'book_close_date', 'Firm']]
        # Connect Database
        conn = sqlite3.connect('mutual_fund.db')
        df.to_sql("daily_nav", conn, if_exists="append", index=False)

        print(f'read-{years}-{months}-success')

years = '2553'
months = ['12', '11', '10', '09', '08',
          '07',  '05', '04', '03', '02', '01']

read_txt(years, months)

# ['06','05','04','03','02','01']
# ['12','11','10','09','08','07']
# ['12','11','10','09','08','07','06','05','04','03','02','01']
# +++++++++++++++++++++++++++++++++++++++
# Master Source Code
# ['06','05','04','03','02','01']
# This will not run on online IDE


URL = "http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/05/2562&date2=31/05/2562"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

soup = soup.find("body")
print(soup.prettify())

data = soup.prettify()

print(len(data))

# write data to text file
f = open('temp.txt', 'w', encoding='utf-8')
f.write(str(data))
f.close()
print('success')

# +++++++++++++++++++++++++++++++++++++++++++++

# v+++++++++++++++++++++++++++++++++++++++


def news():
    # the target we want to open
    url = 'http://www.thaimutualfund.com/AIMC/aimc_navCenterDownloadRepRep.jsp?date1=01/04/2562&date2=05/04/2562'

    # open with GET method
    resp = requests.get(url)

    # http_respone 200 means OK status
    if resp.status_code == 200:
        print("Successfully opened the web page")
        print("The news are as follow :-\n")

        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')

        # l is the list which contains all the text i.e news
        l = soup.find("body")

        # now we want to print only the text part of the anchor.
        # find all the elements of a, i.e anchor
        for i in l.findAll("pre"):
            print(i.text)
    else:
        print("Error")


news()


# +++++++++++++++++++++++++++++++++

# ทดสอบดึง NAV รายวัน

# http://oldweb.aimc.or.th/performance.html
# http://gllt.morningstar.com/dnr0n7f73m/fundquickrank/default.aspx?LanguageId=en-TH
URL = "http://gllt.morningstar.com/dnr0n7f73m/fundquickrank/default.aspx?LanguageId=en-TH"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

soup = soup.find("table")
print(soup.prettify())

data = soup.prettify()

print(len(data))
# write data to text file
f = open('table.txt', 'w', encoding='utf-8')
f.write(str(data))
f.close()
print('success')


# +++++++++++++++++++++++++++++++++++++++

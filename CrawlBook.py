import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

res = requests.get("http://www.eslite.com/sale_top.aspx?cate=156")
soup = BeautifulSoup(res.text,'html.parser')
link = soup.find_all('a', id=re.compile('^ctl00_ContentPlaceHolder1_top50_top50List'))

books = pd.Series()
booksln = pd.Series()
for book in link:
    books = books.append(pd.Series([book.text])).reset_index(drop=True)
    booksln = booksln.append(pd.Series(book.get('href'))).reset_index(drop=True)
#去除重複後取代原本的series
booksln.drop_duplicates(keep='first', inplace=True)
#清除不要的資料轉成list
content = [i.strip('\r\n') for i in books if '\r\n' in i]
top = 1
for title, ln in zip(content, booksln):
    print('TOP',top, ':', title.strip())
    print(ln)
    top += 1

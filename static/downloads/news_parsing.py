
""""news_parsing_example.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1opFm_4DSr-NECmPS0BhmW7aTrxYN9Zvr

Importing the necessary libraries
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

"""Collecting Data"""

url = 'https://www.wired.com/tag/computer-science/'

response = requests.get(url)
print(response)

bs = BeautifulSoup(response.text,"lxml")
print(bs)

temp = bs.find_all('h3', 'SummaryItemHedBase-hiFYpQ iYevEK summary-item__hed')
print(temp)

temp_h2 = temp[0]
a_tag = temp_h2.find('a')
if a_tag:
    print(f"h2 содержит внутри себя тег <a> c ссылкой и сам текст")
    print(f"текст самого первого заголовка: {temp_h2.text}")
    print(f"Ссылка, которая хранится внутри: {a_tag.get('href')}")
else:
    print("Тег <a> не найден внутри первого заголовка h2.")

dict_news = {"news": [], "links": []}

for i in temp:
    dict_news["news"].append(i.text)
    a_tag = i.find('a')
    if a_tag:
        dict_news["links"].append(a_tag.get('href'))
    else:
        dict_news["links"].append("No link found")

df_news = pd.DataFrame(dict_news, columns=["news"])

df_news
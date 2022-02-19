import requests
from bs4 import BeautifulSoup

mysrc = requests.get("http://192.168.144.16:888/emplist")
soup = BeautifulSoup(mysrc.text, 'html.parser')
print(mysrc.text)
print("------------------------------------------------------------------------")
mytables = soup.select("table")

mytable = soup.select("table")[0]

trs = mytable.select("tr")

for idx, tr in enumerate(trs):
    if idx > 0:
        td4 = tr.select("td")
        print(td4[0].text, td4[1].text, td4[2].text, td4[3].text)
        
import requests
from bs4 import BeautifulSoup

mysrc = requests.get("http://192.168.144.16:888/emplist")
soup = BeautifulSoup(mysrc.text, 'html.parser')
print(mysrc.text)
print("------------------------------------------------------------------------")
mytable = soup.find_all("table")[0]
trs = mytable.find_all("tr")

for idx, i in enumerate(trs):
    if idx > 0:
        tds = i.find_all("td")
        print(tds[0].text, end="\t")
        # print(tds[1].text, end="\t")
        # print(tds[2].text, end="\t")
        # print(tds[3].text)
    
import requests
from bs4 import BeautifulSoup

mysrc = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
mysrc.encoding = 'euc-kr'

soup = BeautifulSoup(mysrc.text, 'html.parser', from_encoding='utf-8')
# print(mysrc.text)
print("------------------------------------------------------------------------")

sts = soup.select('.st2')
mya = soup.select('.st2 > a')

for st2 in sts:
    myparent = st2.parent
    tds = myparent.select('td')
    s_name = tds[0].text
    s_code = tds[0].a['title']
    s_price = tds[1].text
    print(s_name, s_code, s_price)

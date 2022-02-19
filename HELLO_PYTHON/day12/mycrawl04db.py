import requests
from bs4 import BeautifulSoup
import datetime
from day12.daostock import DaoStock

stock = DaoStock()

ymd_hm = datetime.datetime.now().strftime("%Y%m%d_%H%M")
mysrc = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
mysrc.encoding = 'euc-kr'


soup = BeautifulSoup(mysrc.text, 'html.parser', from_encoding='utf-8')
# print(mysrc.text)
print("------------------------------------------------------------------------")

sts = soup.select('.st2')
mya = soup.select('.st2 > a')

for idx, st2 in enumerate(sts):
    myparent = st2.parent
    tds = myparent.select('td')
    s_name = tds[0].text
    s_code = tds[0].a['title']
    s_price = tds[1].text.replace(',', '')
    print(idx, s_name, s_code, s_price, ymd_hm)
    stock.myinsert(s_code, s_name, s_price, ymd_hm)
    

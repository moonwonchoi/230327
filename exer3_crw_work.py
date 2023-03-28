#pip install requests
#pip3 install requests
import requests
from bs4 import BeautifulSoup
site = requests.get("https://m.stock.naver.com/marketindex/home/major/exchange/bond")
html = site.text
parser = BeautifulSoup(html, "html.parser")

getTarget = parser.select_one("span.MainListItem_price__dP8R6")

print(getTarget.getText())

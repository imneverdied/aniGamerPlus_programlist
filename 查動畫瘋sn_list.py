import requests
from bs4 import BeautifulSoup

url = 'https://ani.gamer.com.tw/'
headers = {'user-agent': 'Mozilla/5.0'}

r = requests.get(url, headers=headers)  # 將此頁面的HTML GET下來
soup = BeautifulSoup(r.text, "html.parser")  # 將網頁資料以html.parser
# 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
sel = soup.select("div.programlist-block a")

f = open('sn_list.txt', 'w+', encoding='utf-8')
for s in sel:
    動畫名稱 = s.select("div.text-anime-detail p")
    取sn = s["href"].split('=')
    print(取sn[1]+" all #" + 動畫名稱[0].text)  # 字串處理寫入txt
    f.write(取sn[1]+" all #" + 動畫名稱[0].text+"\n")


f.close()

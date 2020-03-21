import urllib.request
import re

url = "https://cn.investing.com/crypto/currency-pairs"

request = urllib.request.Request(url)
#模拟Mozilla浏览器进行爬虫
request.add_header("user-agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
content2 = response2.read().decode('utf-8')
print(len(content2))

urlpattern = "href='([^']+?)'>([^><]+?)</a>.+?\"left\">([^><]+?)</td>.+?pid-([^-]+?)-last"
row_matchs = re.finditer(urlpattern,str(content2),re.S)
count = 0
for cell_matchs in row_matchs:
    urlstr = str(cell_matchs.group(1))
    symbol = (str(cell_matchs.group(2)) + "@" + str(cell_matchs.group(3))).replace(" ","").replace("/","").replace(".","").replace("-","").upper()
    #market = str(cell_matchs.group(3))
    symbol_id = str(cell_matchs.group(4))
    if "crypto" in urlstr or "indices" in urlstr:
        count += 1
        print(str(count) + " " + urlstr + " " + symbol + " " + symbol_id)

f = open("crypto.html", 'w', encoding='utf-8')
f.write(content2)
f.close()
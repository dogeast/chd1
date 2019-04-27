import requests
from lxml import etree
import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root',
                       passwd='Chenhaodong123@', db='chd',charset='utf8')

cur = conn.cursor()

for i in range(0, 10):
    url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    res = requests.get(url)

    tree = etree.HTML(res.text)
    top250 = tree.xpath('//span[@class="title"][1]/text()')
    cur.execute("INSERT INTO yuapp_art (url,content) VALUES (%s,%s)", (url, str(top250)))

cur.close()
conn.commit()
conn.close()

import requests
from bs4 import BeautifulSoup
import MySQLdb
import time
def get_movies():
    conn=MySQLdb.connect(host="localhost",user="root",passwd="gjj8897",db="python_crawler",charset="utf8")
    cur=conn.cursor()
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64;x64)AppleWebKit/537.36 (KHTML,like Gecko) Chrome/52..02743.82 Safari/537.36','Host':'movie.douban.com'}
    for i in range(0,10):
        link='https://movie.douban.com/top250?start='+str(i*25)
        r=requests.get(link,headers=headers,timeout=10)
        soup=BeautifulSoup(r.text,"lxml")
        div_list=soup.find_all('div',class_='info')
        for each in div_list:
            url=each.div.a['href']
            title=each.div.a.span.text.strip()
            synopsis=each.contents[3].p.get_text().strip()
            now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            cur.execute("insert into crawler_movies(name,url,synopsis,time) values(%s,%s,%s,%s)",(title,url,synopsis,now))
    print("电影爬取成功！")
    cur.close()
    conn.commit()
    conn.close()
get_movies()

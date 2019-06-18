from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import MySQLdb
def get_weather():
    conn=MySQLdb.connect(host="localhost",user="root",passwd="gjj8897",db="test1",charset="utf8")
    cur=conn.cursor()
    for i in range(0,9):
        for j in range(0,9):
            resp=urlopen('http://www.weather.com.cn/weather/101'+str(i)+str(j)+'0101.shtml')
            soup=BeautifulSoup(resp,'html.parser')
            try:
                tagCity=soup.find('div',class_="crumbs fl")
                city=tagCity.text.replace('\n','').strip()
                tagDate=soup.find('ul', class_="t clearfix")
                dates=tagDate.h1.string
                tagToday=soup.find('p', class_="tem")
                try:
                    temperatureHigh=tagToday.span.string
                except AttributeError:
                    temperatureHigh=tagToday.find_next('p', class_="tem").span.string
                temperatureLow=tagToday.i.string
                weather=soup.find('p', class_="wea").string
                tagWind=soup.find('p',class_="win")
                winL=tagWind.i.string
                cur.execute("insert into crawler_weathers(city,dates,winL,temperatureLow,temperatureHigh,weather) values(%s,%s,%s,%s,%s,%s)"\
                ,(city,dates,winL,temperatureLow,temperatureHigh,weather))
            except:
                print("")
    print("天气爬取成功！")
    cur.close()
    conn.commit()
    conn.close()
get_weather()

from urllib import parse
import re
import time
from selenium import webdriver
import os
from lxml import etree
import MySQLdb

def get_phones(str):
    conn=MySQLdb.connect(host="localhost",user="root",passwd="gjj8897",db="python_crawler",charset="utf8")
    cur=conn.cursor()
    #如果没有配置chromedriver.exe的环境变量，要写完整路径
    chromedriver = ".\chromedriver.exe"
    browser = webdriver.Chrome(chromedriver)
    url = "https://www.jd.com/"
    browser.get(url)
    time.sleep(1)
    #搜索手机
    phoneLogin = browser.find_element_by_xpath('//*[@id="key"]')
    phoneLogin.send_keys(str)
    time.sleep(1)
    # 搜索
    #//*[@id="search"]/div/div[2]/button
    btnNext = browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
    btnNext.click()
    time.sleep(1)
    for i in range(5):
        #加上延迟时间，不然可能拿不到数据
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 执行JavaScript实现网页下拉倒底部
        time.sleep(2)
        page = browser.page_source
        html = etree.HTML(page)
        links = html.xpath("//*[@id='J_goodsList']/ul[@class='gl-warp clearfix']")
        for link in links:
            # 通过xpath获取商品链接
            #//*[@id="J_goodsList"]/ul/li[5]/div/div[1]/a
            verlink = link.xpath("./li[@class='gl-item']/div[@class='gl-i-wrap']/div[@class='p-img']/a/@href")
            verlink = [parse.urljoin(browser.current_url,i) for i in verlink]
            #通过xpath获取商品价格
            #//*[@id="J_goodsList"]/ul/li[60]/div/div[3]/strong/i
            price = link.xpath("./li[@class='gl-item']/div[@class='gl-i-wrap']/div[@class='p-price']/strong")
            price = [item.xpath('string(.)') for item in price]
            #通过xpath获取商品名称
            #//*[@id="J_goodsList"]/ul/li[8]/div/div[4]/a/em
            name=link.xpath("//div[@class='gl-i-wrap']/div[4]/a/em")
            name = [item.xpath('string(.)') for item in name]
        for i in range(len(verlink)):
            Name=name[i]
            Href=verlink[i]
            Price=price[i]
            now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            cur.execute("insert into crawler_phones(name,url,price,time) values(%s,%s,%s,%s)",(Name,Href,Price,now))
        time.sleep(5)
        #//*[@id="J_bottomPage"]/span[1]/a[9]   
        btnnext = browser.find_element_by_class_name("pn-next")
        print(btnnext)
        btnnext.click()
    
    print("手机爬取成功！")
    cur.close()
    conn.commit()
    conn.close()

get_phones('小米9')

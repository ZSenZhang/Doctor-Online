# -*- coding: utf-8 -*-
import scrapy
import urllib
import hashlib
import os, os.path
import pymysql
from scrapy.http import Request
from selenium import webdriver
from dingxys.items import DingxysItem

filename = u'dingxys_medicine.txt'
fo = open(filename, 'a')
fo.write("data of scrapy")
fo.write("\n")
fo.write("start")
fo.write("\n")

class DingxysSpiderSpider(scrapy.Spider):
    name = 'dingxys_spider'
    allowed_domains = ['yao.dxy.com']
    start_urls = ['http://yao.dxy.com/']

    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path = "/usr/local/bin/phantomjs")
    
    def __del__(self):
        self.driver.quit()
    

    def _url_params(self, url):
        result=urlparse.urlparse(url)
        return urlparse.parse_qs(result.query,True)

    def parse(self,response):
        for sub_1 in response.xpath("//div[@class='drugs-sider']"):
            classification = sub_1.xpath("div/a/text()").extract()[0]
            for sub_2 in response.xpath("//div[@class='drugs-main']/div[@id='drugs-list-box']/ul/li"):
                item = DingxysItem()
                item['classification'] = classification
                tmp = sub_2.xpath("./div/a")
                item['specify'] = tmp.xpath("text()").extract()[0]
                medicine_url = tmp.xpath("@href").extract()[0]
                yield Request(medicine_url, callback=self.parse_medicine, meta={'item': item})

    def parse_medicine(self,response):
        for subm_1 in response.xpath("//div[@class='drugs-ser-list']/div[@class='item']/h3/a"):
            subm_url = subm_1.xpath("@href").extract()[0]
            yield Request(subm_url, callback=self.parse_medicine_detail, meta = {'item': response.meta['item']})

    def parse_medicine_detail(self, response):
        medicine_item = response.meta['item']
        classification = medicine_item['classification']
        specify = medicine_item['specify']
        common_name = response.xpath("//div[@class='content-drugs-describe']/div[@class='item'][1]/p[@class='info'][1]/text()").extract()[0]
        trade_name = response.xpath("//div[@class='content-drugs-describe']/div[@class='item'][1]/p[@class='info'][2]/text()").extract()[0]
        adaptation = response.xpath("//div[@class='content-drugs-describe']/div[@class='item'][4]/p/text()").extract()[0]
        item = DingxysItem()
        item['classification'] = classification
        item['specify'] = specify
        item['common_name'] = common_name
        item['trade_name'] = trade_name
        item['adaptation'] = adaptation


        fo = open(filename, 'a')
        fo.write(item['classification']+";")
        fo.write(item['specify']+";")
        fo.write(item['common_name']+";")
        fo.write(item['trade_name']+";")
        fo.write(item['adaptation']+"\n")
        #fo.write("\n")
        fo.close()

        yield item
    """
    def database(self,item,spider):    #调用这个自定义函数来实现对数据库的操作  
        "
        self.connect = pymysql.connect(  
            user = "root",  
            password = "passwd",  #连接数据库
            port = 3306,  
            host = "127.0.0.1",  
            db = "dingxys",  
            charset = "utf8"  
            )  
        self.cursor = self.connect.cursor()  #获取游标  
        
        con.execute("create database w_dingxys")  #创建数据库，！！！！这一条代码仅限第一次使用，有了数据库后就不用再使用了  
        con.execute("use w_dingxys")   #使用数据库  
        con.execute("drop table if exists dingxys")  #判断是否存在这个数据库表  
        sql = '''''create table dingxys(classification varchar(40),specify varchar(40),common_name varchar(40),trade_name varchar(40),adaptation varchar(200))'''  
        con.execute(sql)  #执行sql命令  创建t_zhaopin表来保存信息  
        
        with open(/home/piggybear/spider/dingxys,"dingxys_medicine.txt") as f:  #打开path本地文档   
            while True:  
                info = f.readline()   #一行一行的读取文档信息  
                if info:  
                    info = info.strip()  #去掉换行符  
                    info = info.split(";")  #以;来分割将信息变换为列表形式  
                    classification = info[0]  
                    specify = info[1]  
                    common_name = info[2]  
                    trade_name = info[3]  
                    adaptation = info[4]  
                    self.cursor.execute("insert into dingxysdrug(classification,specify,common_name,trade_name,adaptation)values(%s,%s,%s,%s,%s)",[classification,specify,common_name,trade_name,adaptation])  
                    # 这一句就是将信息保存至dingxys表中  
                else:  
                    break  
        connect.commit()   #我们需要提交数据库，否则数据还是不能上传的  
        self.cursor.close()   #关闭游标  
        connect.close()  #关闭数据库  
        print("Over!!!!!!!!!") 
    """


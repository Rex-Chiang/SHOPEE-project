import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import MySQLdb
from bs4 import BeautifulSoup as soup

class Crawler:
    def __init__(self, url):
        headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                   'cookie':'_ga=GA1.2.1566855546.1524044064; cto_lwid=cd58dcca-b39b-4ac2-b15d-2110313dbf75; SPC_IA=-1; SPC_F=ICH7TX0k8n7Wvlab2S8GIA5XbiguE485; REC_T_ID=ae848d90-42eb-11e8-b546-d09466041866; __BWfp=c1524044065156xa833f23c6; _atrk_siteuid=86s-Qlcp39HTj8gh; csrftoken=YTZI6Rgb2ySyaB8NXjMxtkKUaIaUiK67; __utma=88845529.1566855546.1524044064.1525406154.1544696703.2; __utmz=88845529.1544696703.2.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _med=refer; _gcl_au=1.1.2067971644.1553094800; _gid=GA1.2.1906412661.1556109629; SC_DFP=0eIM6W8c6PbvBnA20cNHTdxwMXQ7y6UV; SPC_T_ID="W5U6a3wZSLaatJuBQiKkWh9hdj4T9YSHmszKZRANR5xbvxxnJkOmpEifeuiqXgD9pr/ped6GM9uNPmB4GDc2DHJIjGE0zPGVYQMCWKAwlxM="; SPC_SI=qz1a3836o1ruj9kmuov7k66kantz584i; SPC_U=-; SPC_T_IV="HPLurDU1dvmN7amQZV8Dtg=="; SPC_EC=-; welcomePkgShown=true; bannerShown=true; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-61915057-6=1; criteo_write_test=ChUIBBINbXlHb29nbGVSdGJJZBgBIAE',
                   'referer':'https://shopee.tw/shop/829655/search?page=0&sortBy=ctime'}
        self.url = url
        html = requests.get(self.url, headers=headers) # 對網站發出請求
        self.data = json.loads(html.text)#soup(html.text,'html.parser') # 解析html
        
    def products(self):
        #prodict_id = []
        #view_count = []
        #liked_count = []
        #month_sold = []
        #price = []
        #rating_star = []
        #historical_sold = []
        Data = [{},{},{}]
        Img = [{},{},{}]
        
        if self.data["show_disclaimer"] == False:
            items = self.data["items"]
            
            conn = MySQLdb.connect(user='rex',passwd="1209",db="SHOPEE")

            cur = conn.cursor()
            cur.execute("INSERT INTO SHOPEE.shops (shop_id) VALUES (%s)", (int(items[0]["shopid"])))
            print(cur.fetchall())
            cur.close()
            for i in range(3):
                #prodict_id.append(items[i]["itemid"])
                #view_count.append(items[i]["view_count"])
                #liked_count.append(items[i]["liked_count"])
                #month_sold.append(items[i]["sold"])
                #historical_sold.append(items[i]["historical_sold"])
                #rating_star.append(items[i]["item_rating"]["rating_star"])
                #price.append(items[i]["price"]//100000)
                
                Data[i]["prodict_id"] = items[i]["itemid"]
                Data[i]["view_count"] = items[i]["view_count"]
                Data[i]["liked_count"] = items[i]["liked_count"]
                Data[i]["month_sold"] = items[i]["sold"]
                Data[i]["historical_sold"] = items[i]["historical_sold"]
                Data[i]["rating_star"] = items[i]["item_rating"]["rating_star"]
                Data[i]["price"] = items[i]["price"]//100000
                
                Img[i]["prodict_id"] = items[i]["itemid"]
                Img[i]["image"] = "https://cf.shopee.tw/file/"+ items[i]["image"] + "_tn"
                
                
                #cur.execute("INSERT INTO SHOPEE.products(product_id,view_count,liked_count,\
                #                                         month_sold,historical_sold,rating_star,price\
                #                                         ) VALUES("+str(items[i]["itemid"])+","+str(items[i]["view_count"])+","+
                #                                        str(items[i]["liked_count"])+","+str(items[i]["sold"])+","+
                #                                        str(items[i]["historical_sold"])+","+str(items[i]["item_rating"]["rating_star"])+","+
                #                                        str(items[i]["price"]//100000) + ")")
            
            
        #print(Data)
        #print(Img)
        #DATA = pd.DataFrame(Data)
        return Data
    
    
if __name__ == "__main__":
    
    #shopid = "16634688"
    shopid = "829655"
    #url = "https://shopee.tw/shop/"+shopid+"/search?page=0&sortBy=ctime"
    url = "https://shopee.tw/api/v2/search_items/?by=ctime&limit=30&match_id="+shopid+"&newest=0&order=desc&page_type=shop"
    crawler = Crawler(url)
    crawler.products()

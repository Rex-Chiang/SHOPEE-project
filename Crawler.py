import requests
import json
import time
import MySQLdb

class Crawler:
    # 對蝦皮提出請求並解析商品資訊頁面，以MySQL登入AWS RDS
    def __init__(self, shopid):
        headers = {'user-agent':'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
                   'cookie':'_ga=GA1.2.1566855546.1524044064; cto_lwid=cd58dcca-b39b-4ac2-b15d-2110313dbf75; SPC_IA=-1; SPC_F=ICH7TX0k8n7Wvlab2S8GIA5XbiguE485; REC_T_ID=ae848d90-42eb-11e8-b546-d09466041866; __BWfp=c1524044065156xa833f23c6; _atrk_siteuid=86s-Qlcp39HTj8gh; csrftoken=YTZI6Rgb2ySyaB8NXjMxtkKUaIaUiK67; __utma=88845529.1566855546.1524044064.1525406154.1544696703.2; __utmz=88845529.1544696703.2.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _med=refer; _gcl_au=1.1.2067971644.1553094800; _gid=GA1.2.1906412661.1556109629; SC_DFP=0eIM6W8c6PbvBnA20cNHTdxwMXQ7y6UV; SPC_SI=qz1a3836o1ruj9kmuov7k66kantz584i; welcomePkgShown=true; bannerShown=true; SPC_EC="I4YGJ9HBerB1Z/dczYryvk31ZQ+zAxMtAVwmPV3cp6wyvQSTboHGnmxgCcvL0CNdUCG4A/ihowP3rOqquCYORqHfnSlkvdN9tJsUdT4tvQWYHEX1JS2B1Zm3KBSfIi1CrLPCg/cgd9I51oqHoBmNNwAFx8Y1lze2u548J5KPmsA="; SPC_T_ID="VhsNL6T4vscgJVkdQHOyyYzij6+FsTRI/aTYYN6XfqLCAcamO4uwv6Cz3Phqn+y8fSLDaK/Qoqx7vJ1iMOznh8pmw2oGhZE7DwhA2vWXvK0="; SPC_U=1661940; SPC_T_IV="ZRlthBLdxKYThOa0ZkxBCQ=="; SPC_SC_TK=21c2e8a0edde60e21209a96fc379be7b; SPC_SC_UD=1661940; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-61915057-6=1; REC_MD_20=1556291141; criteo_write_test=ChUIBBINbXlHb29nbGVSdGJJZBgBIAE',
                   'referer':'https://shopee.tw/shop/'+shopid+'/search?page=0&sortBy=ctime',
                   'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                   'if-none-match':'8b06819264cbacce454c2d09861976c8;gzip',
                   'if-none-match-':'55b03-571b0e61ecad8cac9f387103ee738b97'}
        
        self.url = "https://shopee.tw/api/v2/search_items/?by=ctime&limit=30&match_id="+shopid+"&newest=0&order=desc&page_type=shop"
        html = requests.get(self.url, headers=headers) # 對網站發出請求
        self.data = json.loads(html.text)
        self.items = self.data["items"]

        host = "rds-mysql-rex.cscjvvfseets.us-east-1.rds.amazonaws.com"

        file = open('/home/rex/桌面/SHOPEE-project/password','r')
        passwd = file.read().rstrip()
        
        self.conn = MySQLdb.connect(host, port=3306, user='rex', passwd=passwd, db="Shopee")        
        self.cur = self.conn.cursor()
    
    # 以MySQL插入使用者蝦皮賣場ID及名字
    def shops(self):
        # 確認蝦皮反爬蟲是否啟動
        if self.data["show_disclaimer"] == False:
            shop_name = str(input("SHOP NAME : "))
            
            sql = "INSERT INTO Shopee.shops (shop_id,shop_name) VALUES (%s,%s)"
            val = (self.items[0]["shopid"], shop_name)
            self.cur.execute(sql,val)            
            self.conn.commit()
    
    # 以MySQL插入最新商品資訊(只取最新3項)
    # 若資料庫已有重複資料則略過(first = False)
    def products(self, first=False):
        try:
            # 確認蝦皮反爬蟲是否啟動
            if self.data["show_disclaimer"] == False:
                count = 0 
                for i in range(len(self.items)):
                    
                    if count == 3:
                        break
                    elif self.check_item(i) or first==True:
                        sql = "INSERT INTO Shopee.products (shop_id, product_id, view_count, liked_count, month_sold,\
                        historical_sold, rating_star, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        # 包括賣場ID、商品ID、瀏覽次數、喜好次數、月銷售量、歷史銷售量、客戶評分、商品價錢
                        val = (self.items[0]["shopid"],self.items[i]["itemid"],self.items[i]["view_count"],
                               self.items[i]["liked_count"],self.items[i]["sold"],self.items[i]["historical_sold"],
                               self.items[i]["item_rating"]["rating_star"],self.items[i]["price"]//100000)
                        self.cur.execute(sql,val)
                        self.conn.commit()
                        count+=1
    
                    else:
                        pass
        except:
            # 蝦皮反爬蟲啟動
            print("BANG")
            pass
    
    # 以MySQL插入最新商品圖片(只取最新3項)
    # 若資料庫已有重複資料則略過(first = False)
    def images(self, first=False):
        if self.data["show_disclaimer"] == False:
            count = 0 
            for i in range(len(self.items)):
                if count == 3:
                    break
                elif self.check_item(i) or first==True:
                    sql = "INSERT INTO Shopee.images (product_id,img) VALUES (%s,%s)"
                    val = (self.items[i]["itemid"],"https://cf.shopee.tw/file/"+ self.items[i]["image"] + "_tn")
                    self.cur.execute(sql,val)
                    self.conn.commit()
                    count+=1
                else:
                    pass
    
    # 檢查資料庫是否已有重複資料
    def check_item(self, i):
        sql = "SELECT * FROM Shopee.products WHERE product_id IN (%s);"
        val = (self.items[i]["itemid"],)
        self.cur.execute(sql,val)
        return self.cur.fetchall()
    
    # 關閉MySQL連線
    def close(self):
        self.conn.close()
    
    # 完整爬蟲流程    
    def run(self):
        sql = "SELECT * FROM Shopee.shops WHERE shop_id IN (%s);"
        val = (self.items[0]["shopid"],)
        self.cur.execute(sql,val)
        if self.cur.fetchall():
            self.products(first=False)
        else:
            self.shops()
            self.products(first=True)
            self.images(first=True)
        
        
if __name__ == "__main__":
    shopid = ["829655", "16634688", "20364967"]
    for shop in shopid:
        crawler = Crawler(shop)
        crawler.run()
        crawler.close()
        time.sleep(30)


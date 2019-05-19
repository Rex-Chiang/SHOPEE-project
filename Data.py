import MySQLdb
import matplotlib.pyplot as plt
import os
from Figure import Figure
from urllib.request import urlretrieve
plt.style.use('ggplot')

class Data:
    def __init__(self, shopid, num):
        self.shopid = shopid
        self.num = num
        
        host = "rds-mysql-rex.cscjvvfseets.us-east-1.rds.amazonaws.com"
        file = open('/home/rex/桌面/SHOPEE-project/password','r')
        passwd = file.read().rstrip()
        
        self.conn = MySQLdb.connect(host, port=3306, user='rex', passwd=passwd, db="Shopee")        
        
        self.cur = self.conn.cursor()
        
    def Get_data(self, product_id):

        sql = "SELECT * FROM Shopee.products WHERE product_id IN ((%s));"
        val = (product_id,)
        self.cur.execute(sql,val)            
        self.conn.commit()
        prd = self.cur.fetchall()
        
        view_count = [x[2] for x in prd]
        liked_count = [x[3] for x in prd]
        month_solds = [x[4] for x in prd]
        historical_solds = [x[5] for x in prd]
        rating_star = [x[6] for x in prd]
        Date = [x[8] for x in prd]
        
        return view_count, liked_count, month_solds, historical_solds, rating_star, Date
    
    def Get_products(self):
        sql = "SELECT product_id FROM products WHERE shop_id = ((%s)) Limit 3;"
        val = (self.shopid,)
        self.cur.execute(sql,val)            
        self.conn.commit()
        pro_ids = self.cur.fetchall()
        
        return pro_ids
    
    def Product_image(self, product_id):
        
        sql = "SELECT img FROM images WHERE product_id = ((%s));"
        val = (product_id,)
        self.cur.execute(sql,val)            
        self.conn.commit()
        img = self.cur.fetchone()[0]
        img_path = os.path.join("/home/rex/桌面/SHOPEE-project/ShopeeProject/ShopeeSite/static/Images/"+str(product_id))
        urlretrieve(img, img_path)
    
    def Run(self):
        products_ids =  list(map(lambda x: x[0], self.Get_products()))
        
        product_id = products_ids[self.num-1]
        
        view_count, liked_count, month_solds, historical_solds, rating_star, Date = self.Get_data(product_id)
        
        figures = Figure(self.shopid)
        figures.Plot(view_count, liked_count, month_solds, historical_solds, rating_star, Date)
        
        self.Product_image(product_id)
        
        return products_ids
        
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    shopid = "829655"
    num = 1
    data = Data(shopid, num)
    data.Run()
    data.close()
    
    
    
    
    
    
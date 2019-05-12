import MySQLdb
import matplotlib.pyplot as plt
plt.style.use('ggplot')
"""
TO DO USE pro_id coneect with Get_data ~~
"""
class Data:
    def __init__(self, shopid):
        self.shopid = shopid
        
        host = "rds-mysql-rex.cscjvvfseets.us-east-1.rds.amazonaws.com"
        file = open('/home/rex/桌面/SHOPEE-project/password','r')
        passwd = file.read().rstrip()
        
        self.conn = MySQLdb.connect(host, port=3306, user='rex', passwd=passwd, db="Shopee")        
        
        self.cur = self.conn.cursor()
        
    def Get_data(self):

        sql = "SELECT * FROM Shopee.products WHERE product_id IN ((%s));"
        val = (1966396779,)
        self.cur.execute(sql,val)            
        self.conn.commit()
        prd1 = self.cur.fetchall()
        #self.conn.close()
        
        view_count = [x[2] for x in prd1]
        liked_count = [x[3] for x in prd1]
        month_solds = [x[4] for x in prd1]
        historical_solds = [x[5] for x in prd1]
        rating_star = [x[6] for x in prd1]
        Date = [x[8] for x in prd1]
        
        return view_count, liked_count, month_solds, historical_solds, rating_star, Date

    def Figure(self):
        
        view_count, liked_count, month_solds, historical_solds, rating_star, Date = self.Get_data()
        plt.figure(figsize=(8,8))
        
        plt.subplot(2,2,1)
        plt.plot(Date, view_count,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("View Counts")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Counts")
        
        plt.subplot(2,2,2)
        plt.plot(Date, liked_count,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("Liked Counts")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Counts")
        
        plt.subplot(2,2,3)
        plt.plot(Date, month_solds,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("Month Solds")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Counts")
        
        plt.subplot(2,2,4)
        plt.plot(Date, historical_solds,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("Historical Solds")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Counts")
        
        plt.tight_layout()
        plt.show()

    
    def Get_products(self):
        sql = "SELECT product_id FROM products WHERE shop_id = ((%s)) Limit 3;"
        val = (self.shopid,)
        self.cur.execute(sql,val)            
        self.conn.commit()
        pro_ids = self.cur.fetchall()
        print(pro_ids)
        
        
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    shopid = "829655"
    data = Data(shopid)
    data.Get_products()
    data.close()
    
    
    
    
    
    
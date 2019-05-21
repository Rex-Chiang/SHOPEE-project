import matplotlib.pyplot as plt
plt.style.use('ggplot')

class Figure:
    def __init__(self, shopid):
        self.shopid = shopid
    
    # 分別繪出統計資訊並存取
    def Plot(self, view_count, liked_count, month_solds, historical_solds, rating_star, Date):
        # 瀏覽次數、喜好次數
        plt.figure(figsize=(10,8))        
        plt.subplot(2,1,1)
        plt.plot(Date, view_count,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("View Counts")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Counts")
        
        plt.subplot(2,1,2)
        plt.plot(Date, liked_count,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("Liked Counts")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Counts")
        
        plt.tight_layout()
        
        plt.savefig("/home/rex/桌面/SHOPEE-project/ShopeeProject/ShopeeSite/static/Counts/"+self.shopid)
        plt.show()
        plt.close()
        # 月銷售量、歷史銷售量
        plt.figure(figsize=(10,8))       
        plt.subplot(2,1,1)
        plt.plot(Date, month_solds,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("Month Solds")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Counts")
        
        plt.subplot(2,1,2)
        plt.plot(Date, historical_solds,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("Historical Solds")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Counts")
        
        plt.tight_layout()
        
        plt.savefig("/home/rex/桌面/SHOPEE-project/ShopeeProject/ShopeeSite/static/Solds/"+self.shopid)
        plt.show()
        plt.close()
        # 客戶評分
        plt.figure(figsize=(10,4))
        plt.plot(Date, rating_star,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("Rating Stars")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Stars")
        
        plt.tight_layout()
        
        plt.savefig("/home/rex/桌面/SHOPEE-project/ShopeeProject/ShopeeSite/static/Stars/"+self.shopid)
        plt.show()
        plt.close()

if __name__ == "__main__":
    shopid = "829655"
    data = Figure(shopid)
    #data.Plot()
    
    
    
    
    
    
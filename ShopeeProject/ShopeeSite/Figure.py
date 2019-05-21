import matplotlib.pyplot as plt
import boto3
import io
plt.style.use('ggplot')

class Figure:
    # 登入AWS S3
    def __init__(self, product_id):
        self.product_id = product_id
        
        file = open('/app/ShopeeSite/password','r')
        pass_file = file.readlines()
        aws_key = pass_file[1].rstrip()
        aws_secret = pass_file[2].rstrip() 
        self.bucket = 'shopeestaticfiles'

        self.s3 = boto3.resource('s3', aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)

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
        # 將圖片存取於AWS S3需注意轉換
        img_data = io.BytesIO()        
        plt.savefig(img_data)
        img_data.seek(0)
        img = img_data.read()
        file_name = 'static/Counts/'+str(self.product_id)+'.png'
        self.s3.Object(self.bucket, file_name).put(Body=img)

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
        # 將圖片存取於AWS S3需注意轉換
        img_data = io.BytesIO()        
        plt.savefig(img_data)
        img_data.seek(0)
        img = img_data.read()
        file_name = 'static/Solds/'+str(self.product_id)+'.png'
        self.s3.Object(self.bucket, file_name).put(Body=img)
        
        plt.close()
        # 客戶評分
        plt.figure(figsize=(10,4))
        plt.plot(Date, rating_star,"o-", lw = 1.5, ms = 5, alpha=0.7, mfc='orange')
        plt.title("Rating Stars")
        plt.xticks(rotation = 45)
        plt.xlabel("Date")
        plt.ylabel("Stars")
        
        plt.tight_layout()
        # 將圖片存取於AWS S3需注意轉換
        img_data = io.BytesIO()        
        plt.savefig(img_data)
        img_data.seek(0)
        img = img_data.read()
        file_name = 'static/Stars/'+str(self.product_id)+'.png'
        self.s3.Object(self.bucket, file_name).put(Body=img)
        
        plt.close()

if __name__ == "__main__":
    shopid = "829655"
    data = Figure(shopid)
    #data.Plot()
    
    
    
    
    
    

# SHOPEE-project

**簡介:**

使用者註冊此網站或是以 Facebook 或 Google 登入，

若使用 Facebook 或 Google 登入則取得使用者姓名及大頭貼顯示於首頁，

登入完成後，使用者便可以在網站中輸入 Shopee賣場ID 開始進行商品統計，

以網路爬蟲定期擷取該 Shopee賣場的商品資訊並存放於 Amazon Relational Database Service，

包括該 Shopee賣場商品的商品圖片、瀏覽次數、喜好次數、月銷售量、歷史銷售量、客戶評分等資訊，

待使用者日後登入此網站便可以觀看從註冊當日至目前所統計的商品資訊，商品資訊將會以曲線圖展現於網站，

由於此網站佈署於 Heroku 雲端平台，因此選用 Amazon Simple Storage Service 當作及時存取資料的網路伺服器，

使用者送出資料後，後端便連線至 AWS RDS 並將資訊統計成圖表儲存於 AWS S3 ，再由 AWS S3 擷取並顯示於網站中。

**Introduction:**

User can sign up the website or login with Facebook, Google account.

If user login with Facebook, Google account, then show user picture at the home page.

After user login, user can enter Shopee store ID to statisticize the products.

Web crawler regularly gets products information of the Shopee store and store in the Amazon Relational Database Service.

Including the product image, number of views, favorites, monthly sales, historical sales, customer ratings, etc.

When user login in the future, they can view the product information that displayed on the website.

Since this website is deployed on the Heroku, Amazon Simple Storage Service for timely access to data.

After user enter the product ID, the backend connects to AWS RDS and stores the statistics chart on AWS S3, and display on the website.

**相關技術及工具:**
 * Python
 * Django 
 * Web crawler
 * Linux crontab
 * AWS RDS
 * AWS S3
 * MySQL
 * Facebook Login API
 * Google Login API
 * Heroku
 * Bootstrap

**成果:**

![Result](https://github.com/Rex-Chiang/SHOPEE-project/blob/master/ShopeeProject/Result/Result.gif)

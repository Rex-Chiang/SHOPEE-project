import MySQLdb
import matplotlib.pyplot as plt
plt.style.use('ggplot')

host = "rds-mysql-rex.cscjvvfseets.us-east-1.rds.amazonaws.com"
file = open('/home/rex/桌面/SHOPEE-project/password','r')
passwd = file.read().rstrip()

conn = MySQLdb.connect(host, port=3306, user='rex', passwd=passwd, db="Shopee")        
cur = conn.cursor()

sql = "SELECT * FROM Shopee.products WHERE product_id IN ((%s));"
val = (1966396779,)
cur.execute(sql,val)            
conn.commit()
prd1 = cur.fetchall()
conn.close()

view_count = [x[2] for x in prd1]
liked_count = [x[3] for x in prd1]
month_solds = [x[4] for x in prd1]
historical_solds = [x[5] for x in prd1]
rating_star = [x[6] for x in prd1]
Date = [x[8] for x in prd1]

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

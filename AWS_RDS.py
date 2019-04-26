import MySQLdb

class AWS:
    def __init__(self):
        host = "rds-mysql-rex.cscjvvfseets.us-east-1.rds.amazonaws.com"
        passwd = str(input("PASSWORD : "))
        conn = MySQLdb.connect(host, port=3306, user='rex', passwd=passwd, db="Shopee")
        cur = conn.cursor()
            
        sql = "CREATE TABLE Shopee.shops (shop_id INT PRIMARY KEY, shop_name VARCHAR(255))"
        cur.execute(sql)
        conn.commit()
        
        sql = "CREATE TABLE Shopee.products (shop_id INT, product_id INT, view_count INT,\
        liked_count INT, month_sold INT, historical_sold INT, rating_star FLOAT, price INT,\
        FOREIGN KEY (shop_id) REFERENCES shops (shop_id));"
        cur.execute(sql)
        conn.commit()
        
        sql = "CREATE TABLE Shopee.images (product_id INT, img VARCHAR(255));"
        cur.execute(sql)
        conn.commit()
        
        conn.close()
        

if __name__ == "__main__":
    
    AWS_database = AWS()
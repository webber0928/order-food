import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO menu (title, price, img) VALUES (?, ?, ?)",
            ('皮蛋肉絲炒飯', 90, 'https://friedricehero.com.tw/wp-content/uploads/2021/01/%E7%9A%AE%E8%9B%8B%E8%82%89%E7%B5%B2%E7%82%92%E9%A3%AF.png')
            )

cur.execute("INSERT INTO menu (title, price, img) VALUES (?, ?, ?)",
            ('打拋豬肉炒飯', 85, 'https://friedricehero.com.tw/wp-content/uploads/2021/01/%E6%89%93%E6%8B%8B%E8%B1%AC%E7%82%92%E9%A3%AF.png')
            )

cur.execute("INSERT INTO menu (title, price, img) VALUES (?, ?, ?)",
            ('義大利羅勒雞肉炒飯', 90, 'https://friedricehero.com.tw/wp-content/uploads/2021/01/%E7%BE%A9%E5%A4%A7%E5%88%A9%E7%BE%85%E5%8B%92%E9%9B%9E%E8%82%89%E7%82%92%E9%A3%AF-1.png')
            )

cur.execute("INSERT INTO menu (title, price, img) VALUES (?, ?, ?)",
            ('川味椒麻牛肉炒飯', 85, 'https://friedricehero.com.tw/wp-content/uploads/2021/01/%E5%B7%9D%E5%91%B3%E6%A4%92%E9%BA%BB%E7%89%9B%E8%82%89%E7%82%92%E9%A3%AF.png')
            )

cur.execute("INSERT INTO menu (title, price, img) VALUES (?, ?, ?)",
            ('德國酸菜香腸炒飯', 85, 'https://friedricehero.com.tw/wp-content/uploads/2021/01/%E5%BE%B7%E5%9C%8B%E9%85%B8%E8%8F%9C%E9%A6%99%E8%85%B8%E7%82%92%E9%A3%AF-1.png')
            )

connection.commit()
connection.close()

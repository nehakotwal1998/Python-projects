import sqlite3

con=sqlite3.connect("cakes_db.sqlite3")
cur=con.cursor()
try:
	cur.execute("CREATE TABLE cakes (id INTEGER PRIMARY KEY, flavor TEXT, egg TEXT ,quantity_in_kgs INTEGER, price INTEGER)")
except sqlite3.OperationalError:
	print("table already exists..")
cur.execute("""INSERT INTO cakes VALUES (1, "Bananas", "NO", 1, 250)""")
cur.execute("""INSERT INTO cakes VALUES(2, "Peanut Butter", "yes", 3, 600)""")
cur.execute("""INSERT INTO cakes VALUES(3, "vanilla", "yes", 5, 380)""")
cur.execute("""INSERT INTO cakes VALUES(4, "Ice cream", "yes", 3, 250)""")
cur.execute("""INSERT INTO cakes VALUES(5, "berries", "no",1, 800)""")
cur.execute("""INSERT INTO cakes VALUES(6, "Chocolate", "yes",3, 250)""")

con.commit()

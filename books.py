import sqlite3

con=sqlite3.connect("books_db.sqlite3")
cur=con.cursor() #to execute sql in python this is the package
try:
	cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY , name TEXT, rating INTEGER)")
except sqlite3.OperationalError:
	print("table already exists..")
cur.execute("INSERT into books VALUES (1,' If you could see me now',5)")
cur.execute("INSERT into books VALUES (2,'The book of tomorrow',3)")
cur.execute("INSERT into books VALUES (3,'a place called here',4)")#till here if we execute its wront ony tables formed data isnt there so to put data we use see down

con.commit()#it saves it on the disks
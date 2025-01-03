import sqlite3

con = sqlite3.connect("tejas.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'VS CODE','C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null,'EDGE','C:\Program Files (x86)\Microsoft\Edge\Application.exe')"
# cursor.execute(query)
# con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)


query = "INSERT INTO web_command VALUES (null,'youtube','https://www.youtube.com/')"
cursor.execute(query)
con.commit()


query = "INSERT INTO web_command VALUES (null,'geekforgeeks','https://www.geeksforgeeks.org/')"
cursor.execute(query)
con.commit()


query = "INSERT INTO web_command VALUES (null,'leetcode','https://leetcode.com/')"
cursor.execute(query)
con.commit()
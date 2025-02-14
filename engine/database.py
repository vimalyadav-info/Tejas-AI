import csv
import sqlite3

con = sqlite3.connect("anugat.db")
cursor = con.cursor()


#===>> application commands
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'VS CODE','C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null,'EDGE','C:\Program Files (x86)\Microsoft\Edge\Application.exe')"
# cursor.execute(query)
# con.commit()



#===>> #web commands

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)




query = "INSERT INTO web_command VALUES (null,'copilot','https://copilot.microsoft.com/')"
cursor.execute(query)
con.commit()


#create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200),mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

#===>> csv file add code

        # # Specify the column indices you want to import (0-based index)
        # # Example: Importing the 1st and 3rd columns
        # desired_columns_indices = [2, 12]

        # # Read data from CSV and insert into SQLite table for the desired columns
        # with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
        #     csvreader = csv.reader(csvfile)
        #     for row in csvreader:
        #         selected_data = [row[i] for i in desired_columns_indices]
        #         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

        # # Commit changes and close connection
        # con.commit()
        # con.close()


# query = "INSERT INTO contacts VALUES (null,'priyanshu gangwar','+91 0000000000','null')"
# cursor.execute(query)
# con.commit()

                # query = 'vimal'
                # query = query.strip().lower()

                # cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
                # results = cursor.fetchall()
                # print(results[0][0])

        # query = "INSERT INTO contacts VALUES (null,'vivek sir BCB ','+91 0000000000','null')"
        # cursor.execute(query)
        # con.commit()

        # query = "INSERT INTO contacts VALUES (null,'prakhar yadav ','+91 0000000000','null')"
        # cursor.execute(query)
        # con.commit()

        # query = "INSERT INTO contacts VALUES (null,' HOD roma saxena ','+91 0000000000','null')"
        # cursor.execute(query)
        # con.commit()

        # query = "INSERT INTO contacts VALUES (null,'amit sharma sir BCB','+91 0000000000','null')"
        # cursor.execute(query)
        # con.commit()



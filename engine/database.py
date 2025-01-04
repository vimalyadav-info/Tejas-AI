import sqlite3

con = sqlite3.connect("tejas.db")
cursor = con.cursor()


#application commands
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'VS CODE','C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code.exe')"
cursor.execute(query)
con.commit()

query = "INSERT INTO sys_command VALUES (null,'EDGE','C:\Program Files (x86)\Microsoft\Edge\Application.exe')"
cursor.execute(query)
con.commit()



#web commands

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


query = "INSERT INTO web_command VALUES (null,'jiosaavan','https://www.jiosaavn.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'spotify','https://open.spotify.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'instagram','https://www.instagram.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'facebook','https://www.facebook.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'leetcode','https://www..com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'leetcode','https://leetcode.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'apna college','https://www.apnacollege.in/?msg=not-logged-in')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'google maps','https://www.google.com/maps/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'meesho','https://www.meesho.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'flipkart','https://www.flipkart.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'amazon','https://www.amazon.in/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'gmail','https://mail.google.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'google','https://www.google.com/')"
cursor.execute(query)
con.commit()


query = "INSERT INTO web_command VALUES (null,'google','https://www.twitter.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'linkedin','https://www.linkedin.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'reddit','https://www.reddit.com/')"
cursor.execute(query)
con.commit(),

query = "INSERT INTO web_command VALUES (null,'pinterest','https://www.pinterest.com/')"
cursor.execute(query)
con.commit()
query = "INSERT INTO web_command VALUES (null,'wikipedia','https://www.wikipedia.org/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'netflix','https://www.netflix.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'quora','https://www.quora.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'stak=ckoverflow','https://www.stackoverflow.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'bing','https://www.bing.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'microsoft','https://www.microsoft.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'adobe','https://www.adobe.com/')"
cursor.execute(query)
con.commit()


query = "INSERT INTO web_command VALUES (null,'dropbox','https://www.dropbox.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'zoom','https://www.zoom.us/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'salesforce','https://www.salesforce.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'twitch','https://www.twitch.tv/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'slack','https://www.slack.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'airbnb','https://www.airbnb.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'uber','https://www.uber.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'booking','https://www.booking.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'craigslist','https://www.craigslist.org/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'hulu','https://www.hulu.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'canva','https://www.canva.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'trello','https://www.trello.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'medium','https://www.medium.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'wordpress','https://www.wordpress.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'tumblr','https://www.tumblr.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'shopify','https://www.shopify.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'paypal','https://www.paypal.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'stripe','https://www.stripe.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'zoominfo','https://www.zoominfo.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'cousera','https://www.coursera.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'edx','https://www.edx.org/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'udemy','https://www.udemy.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'khanacademy','https://www.khanacademy.org/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'codeacademy','https://www.codeacademy.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'pluralsight','https://www.pluralsight.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'zillow','https://www.zillow.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'trulia','https://www.trulia.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'robinhood','https://www.robinhood.com/')"
cursor.execute(query)
con.commit()
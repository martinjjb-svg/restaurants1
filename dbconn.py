import mysql.connector
from flask import Flask, render_template

mydb = mysql.connector.connect(
  host="localhost",
  user="Martin",
  password="password",
  database="restaurants"
)

mycursor = mydb.cursor()

def select_all_res():
    mycursor.execute("SELECT * FROM restaurants")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='restaurant')


def select_all_eur_res():
    mycursor.execute("SELECT * FROM restaurants WHERE nationality='European'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='European')


def select_all_asian_res():
    mycursor.execute("SELECT * FROM restaurants WHERE nationality='Asian'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='Asian')


def select_rating_desc():
    mycursor.execute("SELECT * FROM restaurants ORDER By rating desc")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='Rating')


def select_london():
    mycursor.execute("SELECT * FROM restaurants WHERE address LIKE '%London%'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='London')


def select_albans():
    mycursor.execute("SELECT * FROM restaurants WHERE address LIKE '%Albans%'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='Albans')


def select_nerja():
    mycursor.execute("SELECT * FROM restaurants WHERE address LIKE '%Nerja%'")
    value = mycursor.fetchall()
    return render_template("restaurants.html", data=value, name='Nerja')


def select_all():
    mycursor.execute("SELECT * FROM users")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='All')


def martin():
    mycursor.execute("SELECT * FROM users WHERE name='Martin'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Martin')


def karen():
    mycursor.execute("SELECT * FROM users WHERE name='Karen'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Karen')


def jordan():
    mycursor.execute("SELECT * FROM users WHERE name='Jordan'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Jordan')


def hannah():
    mycursor.execute("SELECT * FROM users WHERE name='Hannah'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Hannah')


def rose():
    mycursor.execute("SELECT * FROM users WHERE name='Rose'")
    value = mycursor.fetchall()
    return render_template("users.html", data=value, name='Rose')


def add_fav(name, restaurant, fav_food, fav_drink):
    mycursor = mydb.cursor()
    mycursor.execute(''' INSERT INTO users VALUES(%s,%s,%s,%s)''', (name, restaurant, fav_food, fav_drink))
    mydb.commit()
    mycursor.close()
    return render_template("favourites.html")


def add_res(name, address, nationality, tel, comment, rating):
    mycursor = mydb.cursor()
    print(type(tel))
    print(type(rating))
    mycursor.execute('''INSERT INTO restaurants (name, address, nationality, tel, comment, rating) VALUES(%s,%s,%s,%s,%s,%s)''', (name, address, nationality, tel, comment, rating))
    mydb.commit()
    mycursor.close()
    return render_template("index.html")


'''
sql = "INSERT INTO restaurants (name, address, nationality, tel, comment, rating) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    ('Pizza Express', '1 High St, Harpenden, Albans', 'European, Italian', '01582765714', 'Easy, close to common', '5'),
    ('Aqua Shard', '32 London Bridge St, London', 'European, British', '02030111256', 'Smart fashionable, great views of London', '9')
    ]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")'''


'''
sql = "INSERT INTO users (name, restaurant, fav_food, fav_drink) VALUES (%s, %s, %s, %s)"
val = [
    ('Martin', 'Aqua Shard', 'Scallops', 'Cloudy Bay '),
    ('Karen', 'Aqua Shard', 'Cornish Sea Bass', 'Cabernet'),
    ('Jordan', 'Aqua Shard', 'Beef Fillet', 'Lager'),
    ('Hannah', 'Aqua Shard', 'Beef Fillet', 'Diet Coke'),
    ('Rose', 'Aqua Shard', 'Cornish Sea Bass', 'Juice')
    ]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")'''

# sql = "UPDATE restaurants SET rating = 7 WHERE name = 'Sketch'"
# mycursor.execute(sql)
# mydb.commit()

sql = "DELETE FROM restaurants WHERE address = 'test'"
mycursor.execute(sql)
mydb.commit()

from flask import Flask, render_template, request
import dbconn


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/town/<name>")
def town(name):
    print(name)
    return name


@app.route("/location")
def location():
    return render_template("location.html")


@app.route("/favourites")
def favourites():
    return render_template("favourites.html")


@app.route("/restaurant")
def restaurant():
    return dbconn.select_all_res()


@app.route("/european")
def european():
    return dbconn.select_all_eur_res()


@app.route("/asian")
def asian():
    return dbconn.select_all_asian_res()


@app.route("/rating")
def rating():
    return dbconn.select_rating_desc()


@app.route("/london")
def london():
    return dbconn.select_london()


@app.route("/albans")
def albans():
    return dbconn.select_albans()


@app.route("/nerja")
def nerja():
    return dbconn.select_nerja()


@app.route("/all")
def all():
    return dbconn.select_all()


@app.route("/martin")
def martin():
    return dbconn.martin()


@app.route("/karen")
def karen():
    return dbconn.karen()


@app.route("/jordan")
def jordan():
    return dbconn.jordan()


@app.route("/hannah")
def hannah():
    return dbconn.hannah()


@app.route("/rose")
def rose():
    return dbconn.rose()


@app.route('/add_restaurant')
def add_restaurant():
    return render_template('add_restaurant.html')


@app.route('/res', methods=['POST', 'GET'])
def res():
    if request.method == 'GET':
        return "Add restaurants"

    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        nationality = request.form['nationality']
        tel = request.form['tel']
        comment = request.form['comment']
        rating = request.form['rating']
        return dbconn.add_res(name, address, nationality, tel, comment, rating)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/fav', methods=['POST', 'GET'])
def fav():
    if request.method == 'GET':
        return "Add favourite dishes and drinks via the favourites Form"

    if request.method == 'POST':
        name = request.form['name']
        restaurant = request.form['restaurant']
        fav_food = request.form['fav_food']
        fav_drink = request.form['fav_drink']
        return dbconn.add_fav(name, restaurant, fav_food, fav_drink)


if __name__ == '__main__':
    app.run()
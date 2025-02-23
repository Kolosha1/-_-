from flask import Flask, render_template, request, flash
from db_scripts import DBManager
from dotenv import load_dotenv
load_dotenv()
import os

IMG_PATH= os.path.dirname(__file__) + os.sep + 'static' + os.sep + 'img'

app = Flask(__name__)  # Створюємо веб–додаток Flask
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = DBManager("blog.db")

@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    categories = db.get_categories()
    meals = db.get_meals()
    return render_template("index.html",categories=categories,meals=meals)  # html-сторінка, що повертається у браузер

@app.route("/category/<int:category_id>")  # Вказуємо url-адресу для виклику функції
def category_page(category_id):
    categories = db.get_categories()
    meals = db.get_meals_by_category(category_id)
    return render_template("category.html",categories=categories,meals=meals,category_name=categories[category_id-1][1])  # html-сторінка, що повертається у браузер


@app.route("/meal/<int:meal_id>", methods = ["GET","POST"])  # Вказуємо url-адресу для виклику функції
def meal_page(meal_id):
    categories = db.get_categories()
    meal = db.get_meals_by_id(meal_id)
    meals = db.get_meals_by_category(meal[5])
    if request.method=="POST":
        db.create_order(request.form['name'],request.form['phone_number'],request.form['address'],meal[3],meal[0],request.form['comment'])
        flash("Замовлення створено","alert-warning")
    return render_template("meals.html",categories=categories,meal=meal,meals=meals)

@app.route("/search")  # Вказуємо url-адресу для виклику функції
def search_page():
    categories = db.get_categories()
    query = request.args.get("query",'')
    meals = db.search_meals(query)
    return render_template("category.html",categories=categories,meals=meals,category_name=query)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер в режимі налагодження

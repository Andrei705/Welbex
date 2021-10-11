from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from models import db, Object, text
import psycopg2

connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="object_db")
cursor = connection.cursor()


app = Flask(__name__)
app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/object_db"
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS'] = False


# Миграция базы данных
db.init_app(app)
migrate = Migrate(db=db, app=app)


# Форма для заполнения базы данных
@app.route('/form')
def form():
    return render_template('form.html')


# Запись в базу данных
@app.route('/completion', methods=['POST'])
def completion():
    if request.method == "POST":
        date = request.form['date']
        name = request.form['name']
        quantity = request.form['quantity']
        distance = request.form['distance']
        print(distance)
        completion_db = Object(date=date, name=name, quantity=quantity, distance=distance)
        db.session.add(completion_db)
        db.session.commit()
        return redirect('/form')


# Форма для запроса фильтрации в базе данных
@app.route('/form_filter')
def form_filter():
    return render_template('filtering.html')


# Запрос в базу данных(Фильтрация)
@app.route('/filtering_bd', methods=['POST'])
def filtering_bd():
    page = request.args.get('page', type=int)
    if request.method == "POST":
        column_selection = request.form['column_selection']
        condition = request.form['condition']
        filtering_value = request.form['filtering_value']

        if condition == 'LIKE':
            cursor.execute(f"SELECT * FROM objects WHERE {column_selection} LIKE'%{filtering_value}%'")
        else:
            cursor.execute(f"SELECT * FROM objects WHERE {column_selection}{condition}{filtering_value}")

        result = cursor.fetchall()
        return render_template('outpyt.html', result=result)


if __name__ == "__main__":
    app.run()
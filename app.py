from flask import Flask, render_template, request
from flask_migrate import Migrate
from models import db, Object, text, Pagination


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
        return 'OK'


# Форма для запроса фильтрации в базе данных
@app.route('/form_filter')
def form_filter():
    return render_template('filtering.html')


# Запрос в базу данных(Фильтрация)
@app.route('/filtering_bd', methods=['POST'])
def filtering_bd():
    if request.method == "POST":
        column_selection = request.form['column_selection']
        condition = request.form['condition']
        filtering_value = request.form['filtering_value']
        if condition == 'like':
            result = db.engine.execute(text(f"SELECT * FROM objects WHERE {column_selection} LIKE '%{filtering_value}%'"))
            return render_template('outpyt.html', result=result)
        else:
            result = Object.query.filter(text(f"{column_selection}{condition}{filtering_value}")).all()
            return render_template('outpyt.html', result=result)


if __name__ == "__main__":
    app.run()
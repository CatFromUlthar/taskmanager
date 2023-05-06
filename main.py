from flask import Flask, render_template, request
from database_interactions import DataBaseInteractor
import os

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    interactor = DataBaseInteractor('tasks.db')
    return render_template('index.html', menu=interactor.get_from_database())


if __name__ == '__main__':
    app.run(debug=True)

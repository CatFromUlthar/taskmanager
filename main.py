from flask import Flask, render_template, request, flash, redirect
from database_interactions import DataBaseInteractor
import secrets
from datetime import datetime

app = Flask(__name__, static_url_path='/static')
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=['GET', 'POST'])
def index():
    interactor = DataBaseInteractor('tasks.db')
    if request.method == 'POST' and 'add' in request.form:
        title = request.form['title']
        contents = request.form['contents']
        dt = datetime.now().__str__()[0:-7]
        completed = 'Не выполнено'
        interactor.add_to_database(title, contents, dt, completed)
        flash('Задача добавлена', 'success')
        return redirect('/')
    elif request.method == 'POST' and 'complete' in request.form:
        task_id = request.form['complete']
        interactor.change_task_status(task_id)
        return redirect('/')
    else:
        return render_template('index.html', menu=interactor.get_from_database())


if __name__ == '__main__':
    app.run(debug=True)

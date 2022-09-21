from flask import render_template, redirect, url_for
from app import app
from flask import request

i=''
dist={'01': 'Адыгея', '02': 'Коми'}

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user, text=i)


@app.route('/district', methods=['POST'])
def district():

    global i
    text = request.form['text']
    i = dist[text]
    return redirect(url_for('index'))

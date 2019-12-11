from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

import sqlite3
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('./database/datas.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS lists (expired_date, name)')
    
    if request.method == 'POST':
        c.execute('INSERT INTO lists VALUES (?, ?)', (request.form['something'], request.form['date']))
    datas = c.execute('SELECT * FROM lists')
    datas = [{'name':data[0], 'date':data[1]} for data in datas]
    conn.commit()
    return render_template('index.html', datas=datas)


@app.route('/remove')
def remove():
    conn = sqlite3.connect('./database/datas.db')
    c = conn.cursor()
    if request.method == 'POST':
        c.execute('DELETE FROM lists WHERE name=(?)', request)
    return redirect(url_for('index'))


@app.route('/edit')
def edit():
    return redirect(url_for('index'))


if __name__=="__main__":
    app.run(debug=True, host='localhost', port=10000)

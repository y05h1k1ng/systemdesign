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
    c.execute('CREATE TABLE IF NOT EXISTS lists (id INTEGER PRIMARY KEY AUTOINCREMENT, expired_date STRING, name STRING)')
    
    if request.method == 'POST':
        c.execute('INSERT INTO lists (expired_date, name)VALUES (?, ?)', (request.form['something'], request.form['date']))
    datas = c.execute('SELECT * FROM lists')
    datas = [{'id': data[0], 'name':data[1], 'date':data[2]} for data in datas]
    conn.commit()
    return render_template('index.html', datas=datas)


@app.route('/remove', methods=['POST'])
def remove():
    conn = sqlite3.connect('./database/datas.db')
    c = conn.cursor()
    c.execute('DELETE FROM lists WHERE name=(?)', request.form[''])


@app.route('/edit', methods=['POST'])
def edit():
    conn = sqlite3.connect('./database/datas.db')
    c = conn.cursor()
    c.execute('', )


if __name__=="__main__":
    app.run(debug=True, host='localhost', port=10000)

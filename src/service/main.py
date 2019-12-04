from flask import Flask, render_template, request
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
    datas = json.dumps(list(datas))
    print("[+] datas:", datas)
    conn.commit()
    return render_template('index.html', datas=datas)

if __name__=="__main__":
    app.run(debug=True, host='localhost', port=10000)

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        with open('./database/data', 'a') as f:
            f.write(request.form['something'] + ' ' + request.form['date'] + '\n')
    with open('./database/data', 'r') as f:
        datas = f.read().split('\n')
    return render_template('index.html', datas=datas)

if __name__=="__main__":
    app.run(debug=True, host='localhost', port=10000)

from flask import Flask
import json
import random

app = Flask(__name__)

rains = ["大雨", "洪水", "暴風"]
tsunami = ["津波注意報", "津波警報", "大津波警報"]
earthquake = ["4", "5弱", "5強", "6弱", "6強", "7"]

@app.route('/tsunami', methods=['GET'])
def tsunami_api():
    types = random.choice(tsunami)
    output = {"type": types, "level": 5}
    return json.dumps(output)

@app.route('/rain', methods=['GET'])
def rain_api():
    types = random.choice(rains)
    level = random.randint(0, 5)
    output = {"type": types, "level": level}
    return json.dumps(output)

@app.route('/earthquake', methods=['GET'])
def earthquake_api():
    types = random.choice(earthquake)
    output = {"type": "", "level": types}
    return json.dumps(output)

@app.route('/volcano', methods=['GET'])
def volcano_api():
    level = random.randint(0, 5)
    output = {"type": "噴火警報", "level": level}
    return json.dumps(output)

if __name__=="__main__":
    app.run(debug=True, host='localhost', port=8888)

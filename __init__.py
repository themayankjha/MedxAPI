from flask import Flask,jsonify, make_response
from functions import make_critical

app = Flask(__name__)

@app.route('/getcritical', methods=['GET', 'POST'])
def make_critical_data():
    d = make_critical()
    return make_response(jsonify(d), 200)

if __name__ == '__main__':
    app.debug = True
    app.run()

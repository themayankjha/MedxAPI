from flask import Flask,jsonify, make_response,request
from functions import make_data

app = Flask(__name__)

@app.route('/dataendpoint', methods=['GET', 'POST'])
def makefulldata():
    username=request.args.get("username")
    data = make_data(username)
    return make_response(jsonify(data), 200)

if __name__ == '__main__':
    app.debug = True
    app.run()

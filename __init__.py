from flask import Flask,jsonify, make_response,request
from functions import make_data

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hello :) This is my API"


@app.route('/dataexitpoint', methods=['GET', 'POST'])
def makefulldata():
    try:
        username=request.args.get("username")
        data = make_data(username)
        return make_response(jsonify(data), 200)
    except:
        return "Please send a request Parameter "

@app.route('/dataentrypoint', methods=['GET', 'POST'])
def getfulldata():
    try:
       pass
    except:
        return "Please send a request Parameter "

if __name__ == '__main__':
    app.debug = True
    app.run()

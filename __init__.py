from flask import Flask,jsonify, make_response,request,render_template
from functions import make_data, databaseentry;

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "Hello :) This is my API"


@app.route('/dataexitpoint', methods=['GET'])
def makefulldata():
    try:
        username=request.args.get("username")
        data = make_data(username)
        return make_response(jsonify(data), 200)
    except:
        return "Please send a request Parameter"

@app.route('/dataentrypoint', methods=['GET'])
def getfulldata():
        username=request.args.get("username")
        anemia=request.args.get("anemia")
        diabetes=request.args.get("diabetes")
        bloodpressure=request.args.get("bloodpressure")
        gender=request.args.get("gender")
        message=databaseentry(username,anemia,diabetes,bloodpressure,gender)
        return message

if __name__ == '__main__':
    app.debug = True
    app.run()

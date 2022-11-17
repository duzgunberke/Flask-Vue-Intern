from flask import Flask, jsonify
from flask_cors import CORS

app= Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})


@app.route('/',methods=['GET'])
def greetings():
    return("Hi everyone")


@app.route('/shark',methods=['GET'])
def shark():
    return("This is a Sharkkkk")

if __name__ == '__main__':
    app.run(debug=True)
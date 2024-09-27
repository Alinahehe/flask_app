from flask import Flask
from flask_restful import Api
from routes import InitRouters

app = Flask(__name__)
api = Api(app)

InitRouters(api)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
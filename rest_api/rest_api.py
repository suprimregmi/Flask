from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
    """
        We first initialized api. After that we are making a GET requests that states if anyone hits on this class,
        then it will return Hello World as response on JSON formats.
        
    """
    def __init__(self):
        pass
    def get(self):
        return {
            "Hello":"World"
        }
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

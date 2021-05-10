from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import *
import json
import my_api

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)


class OneKeyArticle(Resource):
    def get(self):
        return {'hello': 'world'}

    def put(self):
        try:
            print(request.data)
            buff = json.loads(request.data)['data']
            print(buff)
            new_buff = my_api.api_main(buff)
            print(new_buff)
            return {'data': new_buff}
        except Exception as error:
            print(error)
            return {'error': error}


api.add_resource(OneKeyArticle, '/')

if __name__ == '__main__':
    app.run(debug=True)

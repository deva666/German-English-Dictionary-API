from werkzeug.exceptions import abort
from translation import TranslationService
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('term',type=str, required=True, location='args')
parser.add_argument('limit', type=int, required=False, location='args')
parser.add_argument('page', type=int, required=False, location='args')

class TranslationResource(Resource):
    translation = TranslationService()
    def get(self):
        args = parser.parse_args()
        term = args['term']       
        limit = args['limit'] or 100
        page = args['page'] or 0
        if limit < 0 or page < 0:
            abort(400)
        result = self.translation.translate(term, limit, page)
        return result

api.add_resource(TranslationResource, '/translate')

if __name__ == '__main__':
    app.run(debug=True)
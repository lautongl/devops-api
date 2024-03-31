from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
from mongoengine.fields import StringField, DateTimeField

app = Flask(__name__)
api = Api(app)
db = MongoEngine(app)

app.config['MONGO_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': '27017',
    'username': '',
    'password': ''
}


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = StringField(required=True, unique=True)
    last_name = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    birth_date = db.DateTimeField(required=True)


class Users(Resource):
    def get(self):
        return {"user": "user 01"}


class User(Resource):
    def post(self):
        return {"message": "test"}

    def get(self, cpf):
        return {"message": "CPF"}


api.add_resource(Users, "/users")
api.add_resource(User, "/user", "/user/<string:cpf>")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

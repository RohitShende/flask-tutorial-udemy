from datetime import timedelta

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from flask_restful_sql_app.item import ItemList, Item
from flask_restful_sql_app.secret import authenticate, identity
from flask_restful_sql_app.user import UserRegister

app = Flask(__name__)
app.secret_key = 'myownsecretkey'
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['JWT_AUTH_URL_RULE'] = '/login'

api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

# register the api's
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run()

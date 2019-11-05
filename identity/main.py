from flask import Flask, request
from mock_datastore import MockDatastore as Datastore
from user import User
app = Flask(__name__)


user = User(Datastore())


@app.route('/user/<user_id>', methods=['GET', 'POST'])
def user_read(user_id):
    if request.method == 'GET':
        user_id = request.values.get('user_id')
        return user.read(user_id)
    if request.method == 'POST':
        name = request.values.get('name')
        email = request.values.get('email')
        return user.create(user_id, name, email)


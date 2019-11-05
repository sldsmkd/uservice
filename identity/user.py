from mock_datastore import MockDatastore as Datastore


class User(object):

    def __init__(self, datastore):
        self._name = None
        self._email = None
        self._datastore = datastore

    def create(self, user_id, name, email):
        try:
            body = {
                "name": name,
                "email": email
            }
            self._datastore.create(user_id, body)
            return "User Created"
        except KeyError:
            return "Conflict: User Exists"

    def read(self, user_id):
        try:
            body = self._datastore.read(user_id)
            return body
        except KeyError:
            return "Not found"

    def update(self, user_id, name, email):
        pass

    def delete(self, user_id):
        pass


if __name__ == '__main__':
    mds = Datastore()
    u = User(mds)


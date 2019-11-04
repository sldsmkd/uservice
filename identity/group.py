from identity.mock_datastore import MockDatastore

class Group(object):
    def __init__(self, group_id, datastore):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def add_user(self, user_id):
        pass

    def remove_user(self, user_id):
        pass

    def user_in_group(self, group_id, user_id):
        pass


if __name__ == '__main__':
    group = Group(1, MockDatastore())

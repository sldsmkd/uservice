import connexion
import datetime
import logging
from connexion import NoContent
from statsd import StatsClient

# gather some metrics
statsd = StatsClient()

# our memory-only storage
USERS = {}

# auth tokens
TOKENS = {
    '123': 'jdoe',
    '456': 'rms'
}


def token_info(access_token) -> dict:
    uid = TOKENS.get(access_token)
    if not uid:
        return None
    return {'uid': uid, 'scope': ['uid']}


@statsd.timer('get_users')
def get_users(limit, email=None):
    return {"users": [user for user in USERS.values() if not email or user['email'] == email][:limit]}


@statsd.timer('get_user')
def get_user(user_id):
    user = USERS.get(user_id)
    return user or ('Not found', 404)


@statsd.timer('put_user')
def put_user(user_id, user):
    exists = user_id in USERS
    user['id'] = user_id
    if exists:
        logging.info('Updating user %s..', user_id)
        USERS[user_id].update(user)
    else:
        logging.info('Creating user %s..', user_id)
        user['created'] = datetime.datetime.utcnow()
        USERS[user_id] = user
    return NoContent, (200 if exists else 201)


@statsd.timer('delete_user')
def delete_user(user_id):
    if user_id in USERS:
        logging.info('Deleting user %s..', user_id)
        del USERS[user_id]
        return NoContent, 204
    else:
        return NoContent, 404


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('user.yaml')


if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080, server='gevent')

import redis

# create the redis connection
r_conn = redis.Redis( host='localhost', port=6379)

def save_data(key, value):
    r_conn.set(key,value)

def load_data(key):
    return r_conn.get(key)

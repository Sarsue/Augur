import redis

# create the redis connection
r = redis.StrictRedis( host='localhost', port=6379)
max_len = 256

def save_data( key, value):
    print("saving")
    r.rpush(key, value)
  # r.ltrim(key, 0, max_len)

def load_data(key):
    return r.lrange('rlist', 0, -1)

import redis

# create the redis connection
#r = redis.StrictRedis( host='localhost', port=6379)
max_len = 256

def save_data( key, value):
    print("Saving{0}",key)
    r = redis.StrictRedis( host='localhost', port=6379)
    r.rpush(key, value)
  # r.ltrim(key, 0, max_len)

def load_data(key):
  r = redis.StrictRedis( host='localhost', port=6379)
  return r.lrange(key, 0, -1)

def show_entries():
  r = redis.StrictRedis( host='localhost', port=6379)
  key_list  = r.keys()
  for key in key_list:
    print(key,r.lrange(key, 0, -1),"\n")

def clean_entries():
  r = redis.StrictRedis( host='localhost', port=6379)
  key_list  = r.keys()
  for key in key_list:
    r.delete(key)
    

if __name__ == "__main__":
  clean_entries()
  show_entries()
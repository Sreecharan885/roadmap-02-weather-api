import redis, os, json

redis_connection_string = os.environ['REDIS_CONN_STRING']

key_expiration_time = 43200 # 12 Hours

def get_from_redis(key):
    r = redis.Redis.from_url(redis_connection_string)
    return json.loads(r.get(key))

def set_to_redis(key,value):
    r = redis.Redis.from_url(redis_connection_string)
    r.setex(key,key_expiration_time,json.dumps(value))
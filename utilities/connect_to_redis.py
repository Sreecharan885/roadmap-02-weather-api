import redis, os, json

redis_connection_string = os.environ['REDIS_CONN_STRING']

key_expiration_time = 43200 # 12 Hours

def get_redis_client():
    client = redis.Redis.from_url(redis_connection_string)
    return client

def conn_to_redis():
    try:
        r = get_redis_client()
        response = r.ping()
        print(response)
        return r, True
    except redis.RedisError as E:
        print("Connectivity to Redis failed")
        return None, False

def get_from_redis(key):
    '''
        Returns
            None for any failure case
            Python object if it exists.
    '''

    r = conn_to_redis()[0]
    if r == None:
        print("Connectivity to Redis failed")
        return None
    value = r.get(key)
    if value is None:
        return None
    else:
        return json.loads(r.get(key))

def set_to_redis(key,value):
    '''
        Returns 
            True if set properly
            False otherwise.
    '''
    r = conn_to_redis()[0]
    if r == None:
        print("Connectivity to Redis failed")
        return False
    r.setex(key,key_expiration_time,json.dumps(value))
    return True
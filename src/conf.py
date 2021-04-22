import pathlib
import os

import redis
import dotenv


BASE_DIR = pathlib.Path('./')

DEBUG = True

if DEBUG:
    dotenv.load_dotenv(pathlib.Path('.dev.env'))
else: 
    dotenv.load_dotenv(pathlib.Path('.env'))

REDIS_HOST = str(os.environ['REDIS_HOST'])
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

SEASONS = ['winter', 'spring', 'summer', 'fall']

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

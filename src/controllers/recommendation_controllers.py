import datetime
import json

from src import conf
from src import util


def build_rec_message(username, year, season):
    if season not in conf.SEASONS:
        raise util.WebServerException('invalid season', 400)
    
    try:
        request_message = {
            'type': 'recommendation_request',
            'msg': json.dumps({
                'timestamp': datetime.datetime.now().timestamp(),
                'username': str(username),
                'recommendation': {
                    'year': int(year),
                    'season': season
                }
            })
        }
        return request_message
    except ValueError:
        raise util.WebServerException('invalid entry', 400)


def search_cache_for_recommendation(username, year, season):
    res = conf.redis_client.get(f"recommendation:{username}:{year}:{season}")


def create_recommendation_request(username, year, season):
    msg = build_rec_message(username, int(year), season)
    msg_id = conf.redis_client.xadd('recommendation_request', msg)


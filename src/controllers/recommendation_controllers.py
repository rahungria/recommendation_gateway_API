import datetime
import json

from src import conf
from src import util


def build_model_request_msg(username, year, season):
    if season not in conf.SEASONS:
        raise util.WebServerException('invalid season', 400)
    
    try:
        request_message = {
            'type': 'create_model',
            'msg': json.dumps({
                'timestamp': datetime.datetime.now().timestamp(),
                'username': str(username),
            })
        }
        return request_message
    except ValueError:
        raise util.WebServerException('invalid entry', 400)


def build_recommendation_request_msg(username, anime_id):
    try:
        return {
            'type': 'get_recommendation',
            'msg': json.dumps({
                'timestamp': datetime.datetime.now().timestamp(),
                'uuid': conf.UUID,
                'username': username,
                'anime_id': int(anime_id),
            })
        }
    except ValueError:
        raise util.WebServerException('invalid body', 400)


def create_model_request(username, year, season):
    msg = build_model_request_msg(username, int(year), season)
    msg_id = conf.redis_client.xadd('create_model', msg)


def get_recomendation_request(username, anime_id):
    msg = build_recommendation_request_msg(username, anime_id)
    conf.redis_client.xadd('get_recommendation', msg)
    res = conf.redis_client.xreadgroup(
        groupname=conf.GROUP_NAME,
        consumername=conf.uuid,
        streams={conf.RECOMMENDATION_RESULT_STREAM: '>'},
        count=0    
    )
    return util.parse_message(res)


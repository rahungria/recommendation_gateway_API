import flask

import src
from src.controllers import recommendation_controllers as controller
from src import util


@src.app.route('/recommendations/', methods=['POST'])
@util.exception_decorator
def create_recommendations():
    try:
        data = flask.request.get_json()
        controller.build_rec_message(data['username'], data['year'], data['season'])
        return {'message': 'building recommendations...'}, 202
    except KeyError:
        raise util.WebServerException('invalid request body', 400)

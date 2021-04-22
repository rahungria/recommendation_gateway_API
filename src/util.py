import json


class WebServerException(Exception):
    def __init__(self, msg, status_code):
        self.msg = msg
        self.status_code = status_code
        super().__init__(msg)


def exception_decorator(func):
    def inner_f(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except WebServerException as e:
            return {'error': e.msg}, e.status_code
    return inner_f

def parse_message(msg):
    return {k.decode('utf-8'):json.loads(i) for k,i in msg.items()}

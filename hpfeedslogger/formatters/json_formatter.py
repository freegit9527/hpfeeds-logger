import json
import datetime


def format(message):
    msg = dict(message)
    msg['timestamp'] = datetime.datetime.isoformat(datetime.datetime.now())
    return json.dumps(msg)

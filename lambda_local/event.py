'''
Copyright 2015-2018 HDE, Inc.
Licensed under MIT.
'''

import json


def read_event(path):
    with open(path) as f:
        event = f.read()
        event = json.loads(event)
        event['body'] = json.dumps(event['body'])
        return event

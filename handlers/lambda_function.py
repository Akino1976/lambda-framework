import json

from typing import Dict, Any


def handle_event(event: Dict[str, Any], context: object):
    return json.dumps(dict(hello='World'))

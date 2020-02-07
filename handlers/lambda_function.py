import logging

from typing import Any, Dict

logger = logging.getLogger(__name__)


def handle_event(event: Dict[str, Any], context: object):
    message = 'Hello {}'.format(event)

    return {
        'message': message
    }

    logger.info('Successfully processed event')

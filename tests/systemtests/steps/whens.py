import os
import sys
import logging

from typing import Any, Dict

import requests

from pytest_bdd import when, parsers

import helpers.utils as utils


logger = logging.getLogger('bi-framework')


@when(parsers.parse('I make a {request_type} request to {url}'))
def make_request(request: Any,
                 request_headers: Dict[str, Any],
                 request_body: Dict[str, Any],
                 request_type: str,
                 base_url: str,
                 url: str):
    logger.info(f'Setting up request url based on the yaml spec:\n{utils.pretty_format(url)}')

    try:
        url = utils.load_with_tags(request, url)
        import pdb; pdb.set_trace()
        logger.info(f'Request url set to:\n{utils.pretty_format(url)}')

        callable = getattr(requests, request_type.lower())

        logger.info(f'Making {request_type} request to:\n{utils.pretty_format(base_url + url)}')

        request.return_value = callable(
            f'{base_url}{url}',
            headers=request_headers,
            json=request_body if request_body else None
        )

        try:
            response = request.return_value.json()
        except ValueError:
            response = request.return_value.text

        LOGGER.info(f'Request response:\n{utils.pretty_format(response)}')

    except Exception as exception:
        msg = f'{type(exception)}\n{exception}'
        logger.info(f'The request raised the exception:\n{utils.pretty_format(msg)}')

        request.raised_exception = exception

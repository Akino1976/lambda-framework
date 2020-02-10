import logging
import os

import yaml

from typing import Any, Dict, List
from pytest_bdd import given, parsers

import helpers.utils as utils
import helpers.aws as aws

logger = logging.getLogger(__name__)


@given(parsers.parse('the entrypoint "{entrypoint_str}"'), target_fixture='entrypoint')
def set_entrypoint(entrypoint_str):
    return entrypoint_str.rsplit('"', 1)


@given(parsers.parse('the command "{command_str}"'), target_fixture='command')
def set_command(command_str):
    return command_str.rsplit('"', 1)


@given(parsers.parse('the bucket {bucket_name} is empty'))
def empty_bucket(bucket_name):
    aws.empty_bucket(bucket_name)


@given(parsers.parse('the request body:\n{yaml_string}'), target_fixture='request_body')
def create_request_body(request: Any, yaml_string: Any) -> Any:
    yaml_string = yaml.load(yaml_string, Loader=yaml.FullLoader)

    logger.info(f'Request body set to:\n{utils.pretty_format(yaml_string)}')

    return yaml_string

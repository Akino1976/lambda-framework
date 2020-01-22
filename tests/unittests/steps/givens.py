import logging

from typing import Dict, Any

from pytest_bdd import given, parsers
from types import ModuleType

import helpers.utils as utils

import yaml

LOGGER = logging.getLogger('app-framework')


@given(parsers.parse('the parameters:\n{yaml_string}'), target_fixture='parameters')
def create_parameters(request: Any, yaml_string: Dict[str, Any]) -> Dict[str, Any]:
    LOGGER.info(f'Parameters set to:\n{utils.pretty_format(yaml_string)}')

    return yaml.load(yaml_string, Loader=yaml.FullLoader)


@given(parsers.parse('the module {module:S}'))
def set_module(module: str):
    LOGGER.info(f'Base module set to {module}')

    pass


@given('a error message in exception table', target_fixture='datadog_instance')
def invoke_datadog():
    insert_data(
        database='Datastore',
        table_name='sqlsp_error_log',
        dataset=exception_log
    )

    datadog_instance = Datadog()

    return datadog_instance

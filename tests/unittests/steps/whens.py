import logging

import importlib
import builtins
import contextlib

from typing import Any, Dict, Callable, List
from types import ModuleType

from pytest_bdd import when, parsers

LOGGER = logging.getLogger('app-framework')


@when(parsers.parse('I call the {callable_path} function'))
def call_callable(request: Any, callable_path: str, parameters: Dict[str, Any], module: ModuleType):
    module = importlib.import_module(module)

    callable = getattr(module, callable_path)

    try:
        request.return_value = callable(**parameters)

    except Exception as exception:
        LOGGER.exception(f'Exception in when calling {callable_path}')

        request.raised_exception = exception

from pytest_bdd import then, parsers
from types import ModuleType
from typing import Any, Dict, Callable, List


@then(parsers.parse('the string to be longer than {length} characters'))
def check_string_length(request, length):
    assert int(length) < len(request.return_value)


@then(parsers.parse('all items contains the key {key}'))
def list_contains_keys(request, key):
    data = request.return_value['data']
    assert len(data) > 0

    for item in data:
        assert key in item.keys()


@then(parsers.parse('the result should contain:\n{yaml_string}'))
def should_contain(request: Any, yaml_string: Any):
    assert yaml_string in request.return_value

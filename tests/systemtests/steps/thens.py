import os
import json

from typing import Any, Dict

import requests

from pytest_bdd import then, parsers


@then(parsers.parse('the return code should be {return_code}'))
def check_return_code(return_code, request):
    if 'ERROR' in request.process.stdoutdata:
        returncode = 1
    else:
        returncode = 0

    assert returncode == int(return_code)


@then(parsers.parse('the HTTP status code should be {status}'))
def http_status(request: Any, status: str):
    """Verify the HTTP status of a response"""
    expected = requests.codes.get(status)

    if not expected:
        raise KeyError(f"The status code '{status}' is invalid and can not be validated against")

    actual = request.return_value.status_code

    assert actual == expected

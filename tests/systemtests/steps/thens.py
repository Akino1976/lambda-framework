import os
import json

from pytest_bdd import then, parsers

@then(parsers.parse('the return code should be {return_code}'))
def check_return_code(return_code, request):
    if 'ERROR' in request.process.stdoutdata:
        returncode = 1
    else:
        returncode = 0

    assert returncode == int(return_code)

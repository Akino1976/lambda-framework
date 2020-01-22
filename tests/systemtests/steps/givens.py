import os

from pytest_bdd import given, parsers

import logging

logger = logging.getLogger(__name__)


@given(parsers.parse('the entrypoint "{entrypoint_str}"'), target_fixture='entrypoint')
def set_entrypoint(entrypoint_str):
    return entrypoint_str.rsplit('"', 1)


@given(parsers.parse('the command "{command_str}"'), target_fixture='command')
def set_command(command_str):
    return command_str.rsplit('"', 1)


@given('the flags <flags>')
@given(parsers.parse('the flags "{flags}"'), target_fixture='flags')
def set_flag(flags):
    return flags

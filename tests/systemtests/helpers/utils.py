import functools
import inspect
import io

from typing import Any, Type, Optional

import yaml


def create_loader(request: Any) -> Type:
    return type('RequestLoader', (yaml.Loader, ), {'_pytest_request': request})


def load_with_tags(request: Any, yaml_string: str) -> Any:
    loader = create_loader(request)

    return yaml.load(io.StringIO(yaml_string), Loader=loader)


def get_context(loader):
    return loader._pytest_request.getfixturevalue('fantestic_context')


def yaml_tag(tag):
    def register_tag(f):
        yaml.Loader.add_multi_constructor(tag, f)

        return f

    return register_tag


@yaml_tag('!Ref')
def references_tag(loader, tag_suffix, node):
    name = loader.construct_scalar(node)

    if tag_suffix in ('', ':Fixture'):
        return loader._pytest_request.getfixturevalue(name)

    context = get_context(loader)

    if tag_suffix == ':Id':
        value = context.identifiers[name]

    elif tag_suffix == ':Db':
        value = context.database[name]

    else:
        raise ContextError(f"'{tag_suffix}' is not a valid context")

    return value

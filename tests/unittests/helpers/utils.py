import pprint
import textwrap

from typing import Dict, Any


def lowercase_keys(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        key.lower(): value
        for key, value
        in data.items()
    }


def pretty_format(obj: Any) -> str:
    if not isinstance(obj, str):
        obj = pprint.pformat(obj)

    return textwrap.indent(obj, ' ' * 4) + '\n'

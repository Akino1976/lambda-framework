import pytest
import datetime

from typing import Dict, Optional, Any, Callable, List

@pytest.fixture
def parameters() -> Dict[str, Any]:
    return dict()


@pytest.fixture
def current_hour():
    return datetime.datetime.now().strftime('%H')


@pytest.fixture
def last_hour():
    return str(int(datetime.datetime.now().strftime('%H')) - 1)

@pytest.fixture
def instantiated_object() -> Optional[Any]:
    return None

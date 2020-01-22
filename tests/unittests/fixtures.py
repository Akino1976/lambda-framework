import pytest
import datetime
from dateutil.tz import *
from typing import Dict, Optional, Any, Callable, List


@pytest.fixture
def mock_s3_fraud_data():
    return [
        {
            'Key': 'somefile',
            'LastModified': datetime.datetime.now(tzlocal()),
            'ETag': 'd2d73ea027864e6b4548d7e07437029e',
            'Size': 1574,
            'StorageClass': 'STANDARD'
        }
    ]


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

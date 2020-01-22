import os
import pytest

from datetime import date
import datetime
import dateutil.relativedelta
from dateutil.tz import *


@pytest.fixture
def headers():
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }


@pytest.fixture
def entrypoint():
    return []


@pytest.fixture
def command():
    return []


@pytest.fixture
def dataset():
    return []


@pytest.fixture
def tablename():
    pass


@pytest.fixture
def flags():
    return []



@pytest.fixture
def conditions():
    return ''


@pytest.fixture
def bucket_name():
    pass


@pytest.fixture
def queue_url():
    pass


@pytest.fixture
def upload_date():
    return date.today().strftime('%Y-%m-%d')


@pytest.fixture
def client():
    pass


@pytest.fixture
def to_date():
    return int((date.today() + dateutil.relativedelta.relativedelta(months=-1)).strftime('%Y%m'))


@pytest.fixture
def none():
    return None


@pytest.fixture
def yesterday_date():
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    return yesterday.strftime('%Y-%m-%d')


@pytest.fixture
def auth_file_name():
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    return f'aggregated-file/aggregated-prod-eu-west-1-1-{yesterday_date}-13-00-24-aa234.ndjson'


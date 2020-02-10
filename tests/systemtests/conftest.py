import time
import requests
import contextlib


def pytest_sessionstart(session):
    """ Sleeps for up to 60 seconds before session.main() is called. """
    for i in range(0, 120):
        print(
            'Waiting for lambdaserver to start: {seconds} seconds waited'
            .format(seconds=(i / 2))
        )
        with contextlib.suppress(Exception):
            response = requests.get(
                'http://lambdaserver/health'
            )
            if response.ok:
                print(
                    'Waited {seconds} seconds for lambdaserver to start'
                    .format(seconds=(i / 2))
                )

                break

        time.sleep(.5)

import os
import logging
import datetime

from typing import (
    List
)

import common.utils as utils

logger = logging.getLogger(__name__)


def get_sdisk_files(location='/Users/serdarakin/Desktop') -> List[str]:
    files = []
    sdisk_files = utils.list_all_filenames(directory=location)

    logger.info(f'Found file {len(sdisk_files)}')

    return sdisk_files



if __name__ == '__main__':
    print(get_sdisk_files())

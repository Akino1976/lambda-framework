import datetime
import os
import logging
import re

from glob import glob
from typing import (
    List,
    Optional,
    Tuple,
    Dict,
    Iterable
)

logger = logging.getLogger(__name__)


def list_all_filenames(directory: str, regex: str='*') -> List[str]:
    if os.path.exists(directory) is False:
        raise Exception(f'Directory dont exists {directory}')

    else:
        all_files = [
            base_path for filepath in os.walk(directory)
            for base_path in glob(os.path.join(filepath[0], regex))
            if os.path.isfile(base_path)
        ]
        return all_files

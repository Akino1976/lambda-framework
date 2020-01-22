import pytest_bdd

from fixtures import *

from steps.givens import *
from steps.whens import *
from steps.thens import *


pytest_bdd.scenarios('features')

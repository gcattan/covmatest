import pytest
from covmatest.utils import is_symmetric_positive_definite


@pytest.fixture
def is_spd():
    return is_symmetric_positive_definite

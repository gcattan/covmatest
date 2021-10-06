import pytest
from pytest import approx
import numpy as np


def is_positive_semi_definite(X):
    cs = X.shape[-1]
    return np.all(np.linalg.eigvals(X.reshape((-1, cs, cs))) >= 0.0)


def is_positive_definite(X):
    cs = X.shape[-1]
    return np.all(np.linalg.eigvals(X.reshape((-1, cs, cs))) > 0.0)


def is_symmetric(X):
    return X == approx(np.swapaxes(X, -2, -1))


@pytest.fixture
def is_spd():
    def _is_spd(X):
        return is_symmetric(X) and is_positive_definite(X)

    return _is_spd


@pytest.fixture
def is_spsd():
    def _is_spsd(X):
        return is_symmetric(X) and is_positive_semi_definite(X)

    return _is_spsd

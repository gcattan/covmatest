from pytest import approx
import numpy as np


def is_positive_definite(X):
    eig_vals = np.linalg.eigvals(X)
    return np.all(eig_vals > 0.0)


def is_symmetric(X):
    symmetric_mat = np.swapaxes(X, -2, -1)
    return X == approx(symmetric_mat)


def is_symmetric_positive_definite(X):
    return is_symmetric(X) and is_positive_definite(X)

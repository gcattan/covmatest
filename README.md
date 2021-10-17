# covmatest

Generate covariance matrices for testing.

## Installation

```
python setup.py develop
```

## Usage

```
from covmatest import get_covmat
n_matrices = 3
n_channels = 2
covmat = get_covmat(n_matrices, n_channels)
print(covmat)
```

## Environment

- Ubuntu, Windows, MacOs
- Python 3.7 and 3.8
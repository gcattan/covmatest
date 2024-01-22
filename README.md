<img type="image/svg" src="https://byob.yarr.is/gcattan/covmatest/score"/>

# covmatest

Generate covariance matrices for testing.

## Installation

- Using pipy:

```
pip install covmatest
```

- For developers:

```
python setup.py develop
```

## Usage

### Example 1
```
from covmatest import get_covmat
n_matrices = 3
n_channels = 2
covmat = get_covmat(n_matrices, n_channels)
print(covmat)
```

### Example 2
```
from covmatest import get_covmat
n_matrices, n_channels = 3, 2
classA = get_covmat(n_matrices, n_channels, seed=None, returns_A=True, returns_B=False)
classB = get_covmat(n_matrices, n_channels, seed=None, returns_A=False, returns_B=True)
```

## Environment

- Ubuntu, Windows, MacOs
- Python 3.8 and 3.9

## How to cite?

G. Cattan, covmatest. 2021. [Online]. Available: https://github.com/gcattan/covmatest/
DOI: https://doi.org/10.5281/zenodo.5574548

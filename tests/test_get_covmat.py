from covmatest import get_covmat, CovmatGen


def test_canary(is_spd):
    get_covmat(1, 1)


def test_allowed_indices():
    for channel in range(1, 17):
        covmat = get_covmat(10, channel)
        assert covmat.shape == (10, channel, channel)


def test_not_allowed_indices():
    for trial in [-1, 0]:
        for channel in [-1, 0, 17]:
            try:
                get_covmat(trial, channel)
                assert False  # should not be possible
            except Exception:
                pass


def test_is_spd(is_spd):
    for channel in range(1, 17):
        assert is_spd(get_covmat(100, channel))


def test_seed():
    covmat1 = get_covmat(1, 1, seed=42)
    covmat1bis = get_covmat(1, 1, seed=42)
    covmat2 = get_covmat(1, 1, seed=43)
    assert not covmat1[0][0] == covmat2[0][0]
    assert covmat1[0][0] == covmat1bis[0][0]


def test_returns_A_B():
    n_matrices, n_channels = 1, 1
    classA = CovmatGen(returns_A=True, returns_B=False).get_covmat(
        n_matrices, n_channels
    )
    classB = CovmatGen(returns_A=False, returns_B=True).get_covmat(
        n_matrices, n_channels
    )
    assert not classA[0][0] == classB[0][0]

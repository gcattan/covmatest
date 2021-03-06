from covmatest import get_covmat


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

from covmatTest import CovmatGen


def test_canary(is_spd, is_spsd):
    CovmatGen().get_covmat(1, 1)


def test_allowed_indices():
    gen = CovmatGen()
    for channel in range(1, 17):
        covmat = gen.get_covmat(10, channel)
        assert covmat.shape == (10, channel, channel)


def test_not_allowed_indices():
    gen = CovmatGen()
    for trial in [-1, 0]:
        for channel in [-1, 0, 17]:
            try:
                gen.get_covmat(trial, channel)
                assert(False)  # should not be possible
            except Exception:
                pass


def test_is_spd(is_spd):
    gen = CovmatGen()
    for channel in range(1, 17):
        assert(is_spd(gen.get_covmat(100, channel)))


def test_is_spsd(is_spsd):
    gen = CovmatGen()
    for channel in range(1, 17):
        assert(is_spsd(gen.get_covmat(100, channel)))

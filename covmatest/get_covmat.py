from pyriemann.estimation import Covariances
from alphawaves.dataset import AlphaWaves
import numpy as np
import mne
import random

"""
=============================
Get a covariance matrice sample from alphawaves dataset
=============================

The CovmatGen generate real covariance matrices which are SDP,
for test purposes.

"""
# Authors: Gregoire Cattan <gcattan@hotmail.com>
#
# License: Apache 2.0

import warnings

warnings.filterwarnings("ignore")

_instance = None


def get_covmat(n_trials, n_channels):
    global _instance
    if _instance is None:
        _instance = CovmatGen()
    return _instance.get_covmat(n_trials, n_channels)


class CovmatGen:

    """Generate test covariance matrices.

    References
    ----------
    [1] Rodrigues PLC. Alpha-Waves-Dataset [Internet].
            Grenoble: GIPSA-lab; 2018. Available from:
            https://github.com/plcrodrigues/Alpha-Waves-Dataset

    [2] Cattan et al., ‘EEG Alpha Waves Dataset’, GIPSA-LAB,
            Research Report, décembre 2018. Available from:
            https://hal.archives-ouvertes.fr/hal-02086581

    """

    def __init__(self):
        self._dataset = AlphaWaves(useMontagePosition=False)
        subject = self._get_random_subject()
        self._raw = self._dataset._get_single_subject_data(subject)
        self._trials = self._get_trials()
        self._n_trials = len(self._trials)
        assert self._n_trials > 0

    def _get_random_subject(self):
        subjects = self._dataset.subject_list
        n_subjects = len(subjects)
        assert n_subjects > 0
        i_subject = random.randint(0, n_subjects - 1)
        subject = subjects[i_subject]
        return subject

    def _get_trials(self):
        events = mne.find_events(raw=self._raw, shortest_event=1, verbose=False)
        event_id = {"closed": 1, "open": 2}
        epochs = mne.Epochs(
            self._raw,
            events,
            event_id,
            tmin=2.0,
            tmax=8.0,
            baseline=None,
            verbose=False,
            preload=True,
        )
        epochs.pick_types(eeg=True)
        return epochs.get_data()

    def _get_covmat(self, n_channels):
        index = random.randint(0, self._n_trials - 1)
        trial = np.array([self._trials[index][:n_channels, :]])
        return Covariances(estimator="lwf").fit_transform(trial)

    def get_covmat(self, n_matrices, n_channels):
        """Get a set of covariance matrices.

        Parameters
        ----------
        n_matrices : int
            The number of covariance matrices to return.
        n_channels: int
            The number of channels (>= 1 and <= 16)
            in a matrix.

        Returns
        -------
        covset : ndarray of int, shape (n_matrices, n_channels, n_channels)
            A set of covariance matrices.
        """
        covset = np.zeros((n_matrices, n_channels, n_channels))
        for i in range(0, n_matrices):
            covset[i] = self._get_covmat(n_channels)
        return covset

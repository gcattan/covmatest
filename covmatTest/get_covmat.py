from pyriemann.estimation import Covariances
from alphawaves.dataset import AlphaWaves
import numpy as np
import mne
import random

"""
=============================
Get a covariance matrice sample from alphawaves dataset
=============================

TODO

"""
# Authors: Gregoire Cattan <gcattan@hotmail.com>
#
# License: Apache 2.0

import warnings
warnings.filterwarnings("ignore")


class CovmatGen():
    def __init__(self):
        self.dataset = AlphaWaves(useMontagePosition=False)
        subject = self._get_random_subject()
        self.raw = self.dataset._get_single_subject_data(subject)
        self.trials = self._get_trials()
        self.n_trials = len(self.trials)
        assert(self.n_trials > 0)

    def _get_random_subject(self):
        subjects = self.dataset.subject_list
        n_subjects = len(subjects)
        assert(n_subjects > 0)
        subject = random.randint(0, n_subjects - 1)
        return subject

    def _get_trials(self):
        events = mne.find_events(raw=self.raw, shortest_event=1, verbose=False)
        event_id = {'closed': 1, 'open': 2}
        epochs = mne.Epochs(self.raw, events, event_id, tmin=2.0, tmax=8.0,
                            baseline=None, verbose=False, preload=True)
        epochs.pick_types(eeg=True)
        return epochs.get_data()

    def _get_covmat(self, n_channels):
        index = random.randint(0, self.n_trials - 1)
        trial = np.array([self.trials[index][:n_channels, :]])
        return Covariances(estimator='lwf').fit_transform(trial)

    def get_covmat(self, n_matrices, n_channels):
        covset = np.zeros((n_matrices, n_channels, n_channels))
        for i in range(0, n_matrices):
            covset[i] = self._get_covmat(n_channels)
        return covset

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

trials = []


def _get_trials(raw):
    events = mne.find_events(raw=raw, shortest_event=1, verbose=False)
    event_id = {'closed': 1, 'open': 2}
    epochs = mne.Epochs(raw, events, event_id, tmin=2.0, tmax=8.0,
                        baseline=None, verbose=False, preload=True)
    epochs.pick_types(eeg=True)
    return epochs.get_data()


def _init():
    dataset = AlphaWaves(useMontagePosition=False)

    subjects = dataset.subject_list
    n_subjects = len(subjects)
    subject = random.randint(0, n_subjects - 1)

    raw = dataset._get_single_subject_data(subject)

    global trials
    trials = _get_trials(raw)
    return len(trials)


def _get_covmat(n_channels):
    global trials
    n_trials = len(trials)
    if n_trials == 0:
        n_trials = _init()
    index = random.randint(0, n_trials - 1)
    trial = np.array([trials[index][:n_channels, :]])
    return Covariances(estimator='lwf').fit_transform(trial)


def get_covmat(n_matrices, n_channels):
    covset = np.zeros((n_matrices, n_channels, n_channels))
    for i in range(0, n_matrices):
        covset[i] = _get_covmat(n_channels)
    return covset

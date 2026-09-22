import numpy as np

from musika.synth import oscillators


def test_sine_has_expected_sample_count():
    signal = oscillators.sine(frequency=440.0, duration=1.0, sample_rate=44100)
    assert len(signal) == 44100


def test_sine_stays_within_unit_amplitude():
    signal = oscillators.sine(frequency=440.0, duration=1.0, sample_rate=44100)
    assert np.max(np.abs(signal)) <= 1.0


def test_square_only_takes_extreme_values():
    signal = oscillators.square(frequency=100.0, duration=0.1, sample_rate=44100)
    assert set(np.unique(signal)).issubset({-1.0, 0.0, 1.0})


def test_white_noise_has_expected_sample_count():
    signal = oscillators.white_noise(duration=0.5, sample_rate=44100)
    assert len(signal) == 22050

import numpy as np

from musika.synth import envelopes


def test_apply_adsr_starts_and_ends_near_silence():
    signal = np.ones(44100)
    envelope = envelopes.Adsr(attack=0.1, decay=0.1, sustain=0.5, release=0.1)

    shaped = envelopes.apply_adsr(signal, envelope, sample_rate=44100)

    assert shaped[0] == 0.0
    assert shaped[-1] < 0.01


def test_apply_adsr_preserves_sample_count():
    signal = np.ones(1000)
    envelope = envelopes.Adsr(attack=0.001, decay=0.001, sustain=0.5, release=0.001)

    shaped = envelopes.apply_adsr(signal, envelope, sample_rate=44100)

    assert len(shaped) == len(signal)

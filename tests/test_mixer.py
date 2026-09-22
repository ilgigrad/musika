import numpy as np
import pytest

from musika.mixing import mixer


def test_mix_sums_tracks_with_gain():
    track_a = mixer.Track(buffer=np.array([0.5, 0.5, 0.5]), gain=1.0)
    track_b = mixer.Track(buffer=np.array([0.1, 0.1, 0.1]), gain=0.5)

    mixed = mixer.mix((track_a, track_b))

    np.testing.assert_allclose(mixed, [0.55, 0.55, 0.55])


def test_mix_normalizes_when_clipping():
    track = mixer.Track(buffer=np.array([1.0, -2.0, 1.0]), gain=1.0)

    mixed = mixer.mix((track,))

    assert np.max(np.abs(mixed)) == pytest.approx(1.0)


def test_mix_requires_at_least_one_track():
    with pytest.raises(ValueError):
        mixer.mix(())

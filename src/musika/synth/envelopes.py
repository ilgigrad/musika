import attrs
import numpy as np


@attrs.frozen
class Adsr:
    attack: float
    decay: float
    sustain: float
    release: float


def apply_adsr(signal: np.ndarray, envelope: Adsr, sample_rate: int) -> np.ndarray:
    """
    Appliquer une enveloppe ADSR (attack/decay/sustain/release) à un signal.
    """
    n_samples = len(signal)
    n_attack = int(envelope.attack * sample_rate)
    n_decay = int(envelope.decay * sample_rate)
    n_release = int(envelope.release * sample_rate)
    n_sustain = max(n_samples - n_attack - n_decay - n_release, 0)

    curve = np.concatenate(
        [
            np.linspace(0, 1, n_attack, endpoint=False),
            np.linspace(1, envelope.sustain, n_decay, endpoint=False),
            np.full(n_sustain, envelope.sustain),
            np.linspace(envelope.sustain, 0, n_release, endpoint=True),
        ]
    )

    if len(curve) < n_samples:
        curve = np.pad(curve, (0, n_samples - len(curve)))
    else:
        curve = curve[:n_samples]

    return signal * curve

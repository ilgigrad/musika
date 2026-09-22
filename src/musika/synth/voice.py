import enum

import attrs
import numpy as np

from musika.synth import envelopes, oscillators


class Waveform(enum.Enum):
    SINE = "sine"
    SAW = "saw"
    SQUARE = "square"


_OSCILLATORS_BY_WAVEFORM = {
    Waveform.SINE: oscillators.sine,
    Waveform.SAW: oscillators.saw,
    Waveform.SQUARE: oscillators.square,
}


@attrs.frozen
class Voice:
    waveform: Waveform
    envelope: envelopes.Adsr

    def render(self, frequency: float, duration: float, sample_rate: int) -> np.ndarray:
        """
        Rendre un buffer audio pour une note jouée par cette voix.
        """
        oscillator = _OSCILLATORS_BY_WAVEFORM[self.waveform]
        signal = oscillator(frequency, duration, sample_rate)
        return envelopes.apply_adsr(signal, self.envelope, sample_rate)

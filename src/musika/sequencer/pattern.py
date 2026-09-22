import attrs
import numpy as np

from musika.sequencer import note as note_
from musika.synth import voice as voice_


@attrs.frozen
class Pattern:
    notes: tuple[note_.Note, ...]

    def duration(self) -> float:
        """
        Retourner la durée totale du pattern, en secondes.
        """
        if not self.notes:
            return 0.0
        return max(n.start + n.duration for n in self.notes)

    def render(self, voice: voice_.Voice, sample_rate: int) -> np.ndarray:
        """
        Rendre ce pattern en un buffer audio joué par la voix passée en paramètre.
        """
        n_samples = int(self.duration() * sample_rate)
        buffer = np.zeros(n_samples)

        for current_note in self.notes:
            rendered = voice.render(current_note.frequency(), current_note.duration, sample_rate)
            rendered = rendered * current_note.velocity

            start_sample = int(current_note.start * sample_rate)
            end_sample = min(start_sample + len(rendered), n_samples)
            buffer[start_sample:end_sample] += rendered[: end_sample - start_sample]

        return buffer

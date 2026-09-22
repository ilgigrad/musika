import attrs

_NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


@attrs.frozen
class Note:
    pitch: str
    start: float
    duration: float
    velocity: float = 1.0

    def frequency(self) -> float:
        """
        Retourner la fréquence (Hz) de cette note, ex: "A4" -> 440.0.
        """
        name = self.pitch[:-1]
        octave = int(self.pitch[-1])
        semitone = _NOTE_NAMES.index(name)
        semitones_from_a4 = semitone - _NOTE_NAMES.index("A") + (octave - 4) * 12
        return 440.0 * (2 ** (semitones_from_a4 / 12))

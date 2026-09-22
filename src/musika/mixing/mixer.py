import pathlib

import attrs
import numpy as np
import soundfile


@attrs.frozen
class Track:
    buffer: np.ndarray
    gain: float = 1.0


def mix(tracks: tuple[Track, ...]) -> np.ndarray:
    """
    Sommer plusieurs pistes (avec leur gain) en un seul buffer stéréo.

    :raises ValueError: si aucune piste n'est passée.
    """
    if not tracks:
        raise ValueError("Au moins une piste est nécessaire pour le mixage")

    length = max(len(track.buffer) for track in tracks)
    mixed = np.zeros(length)

    for track in tracks:
        padded = np.pad(track.buffer, (0, length - len(track.buffer)))
        mixed += padded * track.gain

    peak = np.max(np.abs(mixed))
    if peak > 1.0:
        mixed = mixed / peak

    return mixed


def export(buffer: np.ndarray, path: pathlib.Path, sample_rate: int) -> None:
    """
    Exporter un buffer audio mixé vers un fichier WAV.
    """
    soundfile.write(path, buffer, sample_rate)

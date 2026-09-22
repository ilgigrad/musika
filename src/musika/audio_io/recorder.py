import pathlib

import numpy as np
import sounddevice
import soundfile


def record(duration: float, sample_rate: int, channels: int = 1) -> np.ndarray:
    """
    Enregistrer un buffer audio depuis l'interface audio par défaut du système.

    Nécessite un accès direct au matériel audio : à exécuter en natif sur le
    Mac, jamais dans un conteneur.
    """
    buffer = sounddevice.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=channels,
    )
    sounddevice.wait()
    return buffer.reshape(-1)


def save(buffer: np.ndarray, path: pathlib.Path, sample_rate: int) -> None:
    """
    Sauvegarder un buffer audio dans un fichier WAV.
    """
    soundfile.write(path, buffer, sample_rate)

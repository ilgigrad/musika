import numpy as np


def sine(frequency: float, duration: float, sample_rate: int) -> np.ndarray:
    """
    Générer une onde sinusoïdale.
    """
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)


def saw(frequency: float, duration: float, sample_rate: int) -> np.ndarray:
    """
    Générer une onde en dents de scie.
    """
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    phase = frequency * t
    return 2 * (phase - np.floor(phase + 0.5))


def square(frequency: float, duration: float, sample_rate: int) -> np.ndarray:
    """
    Générer une onde carrée.
    """
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    return np.sign(np.sin(2 * np.pi * frequency * t))


def white_noise(duration: float, sample_rate: int) -> np.ndarray:
    """
    Générer du bruit blanc.
    """
    n_samples = int(duration * sample_rate)
    return np.random.uniform(low=-1.0, high=1.0, size=n_samples)

import pathlib

from musika.mixing import mixer
from musika.sequencer import note as note_
from musika.sequencer import pattern as pattern_
from musika.synth import envelopes, voice

SAMPLE_RATE = 44100


def main() -> None:
    """
    Rendre un petit arpège et l'exporter dans audio/example.wav.
    """
    lead = voice.Voice(
        waveform=voice.Waveform.SAW,
        envelope=envelopes.Adsr(attack=0.01, decay=0.1, sustain=0.6, release=0.2),
    )

    arpeggio = pattern_.Pattern(
        notes=(
            note_.Note(pitch="C4", start=0.0, duration=0.4),
            note_.Note(pitch="E4", start=0.4, duration=0.4),
            note_.Note(pitch="G4", start=0.8, duration=0.4),
            note_.Note(pitch="C5", start=1.2, duration=0.6),
        )
    )

    buffer = arpeggio.render(lead, SAMPLE_RATE)
    mixed = mixer.mix((mixer.Track(buffer=buffer, gain=0.8),))

    output_dir = pathlib.Path(__file__).resolve().parent.parent / "audio"
    output_dir.mkdir(exist_ok=True)
    mixer.export(mixed, output_dir / "example.wav", SAMPLE_RATE)
    print(f"Rendu dans {output_dir / 'example.wav'}")


if __name__ == "__main__":
    main()

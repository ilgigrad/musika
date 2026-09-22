from musika.sequencer import note as note_
from musika.sequencer import pattern as pattern_
from musika.synth import envelopes, voice

SAMPLE_RATE = 44100


def _voice() -> voice.Voice:
    return voice.Voice(
        waveform=voice.Waveform.SINE,
        envelope=envelopes.Adsr(attack=0.01, decay=0.01, sustain=0.8, release=0.01),
    )


def test_pattern_duration_matches_last_note_end():
    notes = (
        note_.Note(pitch="C4", start=0.0, duration=0.5),
        note_.Note(pitch="E4", start=0.5, duration=0.3),
    )
    assert pattern_.Pattern(notes=notes).duration() == 0.8


def test_empty_pattern_has_zero_duration():
    assert pattern_.Pattern(notes=()).duration() == 0.0


def test_render_produces_buffer_matching_duration():
    notes = (note_.Note(pitch="A4", start=0.0, duration=0.5),)
    rendered = pattern_.Pattern(notes=notes).render(_voice(), SAMPLE_RATE)
    assert len(rendered) == int(0.5 * SAMPLE_RATE)

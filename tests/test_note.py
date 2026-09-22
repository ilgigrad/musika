from musika.sequencer import note as note_


def test_a4_frequency_is_440hz():
    assert note_.Note(pitch="A4", start=0.0, duration=1.0).frequency() == 440.0


def test_c4_frequency_is_below_a4():
    c4 = note_.Note(pitch="C4", start=0.0, duration=1.0).frequency()
    assert round(c4, 2) == 261.63


def test_octave_up_doubles_frequency():
    a4 = note_.Note(pitch="A4", start=0.0, duration=1.0).frequency()
    a5 = note_.Note(pitch="A5", start=0.0, duration=1.0).frequency()
    assert a5 == a4 * 2

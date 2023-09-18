import pytest
from project import save_recording, record, recording_to_text


def test_record():
    with pytest.raises(TypeError):
        record("cat")


def test_missing_voice_file():
    with pytest.raises(TypeError):
        recording_to_text()


def test_save_recording():
    with pytest.raises(SystemExit):
        save_recording("n", 48000, "")
    with pytest.raises(SystemExit):
        save_recording("NO", 48000, "")
    with pytest.raises(SystemExit):
        save_recording("no", 48000, "")

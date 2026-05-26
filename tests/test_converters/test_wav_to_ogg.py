from unittest.mock import patch, MagicMock
from avx.converters.wav_to_ogg import convert_wav_to_ogg

@patch('avx.converters.wav_to_ogg.AudioFileClip')
def test_convert_wav_to_ogg(mock_clip):
    """Test wav to ogg conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_wav_to_ogg('input.wav', 'output.ogg')
    mock_clip.assert_called_once_with('input.wav')
    mock_instance.write_audiofile.assert_called_once_with('output.ogg', logger=None)
    mock_instance.close.assert_called_once()

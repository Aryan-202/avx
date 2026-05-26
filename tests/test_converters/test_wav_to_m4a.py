from unittest.mock import patch, MagicMock
from avx.converters.wav_to_m4a import convert_wav_to_m4a

@patch('avx.converters.wav_to_m4a.AudioFileClip')
def test_convert_wav_to_m4a(mock_clip):
    """Test wav to m4a conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_wav_to_m4a('input.wav', 'output.m4a')
    mock_clip.assert_called_once_with('input.wav')
    mock_instance.write_audiofile.assert_called_once_with('output.m4a', logger=None)
    mock_instance.close.assert_called_once()

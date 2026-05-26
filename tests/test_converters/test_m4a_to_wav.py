from unittest.mock import patch, MagicMock
from avx.converters.m4a_to_wav import convert_m4a_to_wav

@patch('avx.converters.m4a_to_wav.AudioFileClip')
def test_convert_m4a_to_wav(mock_clip):
    """Test m4a to wav conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_m4a_to_wav('input.m4a', 'output.wav')
    mock_clip.assert_called_once_with('input.m4a')
    mock_instance.write_audiofile.assert_called_once_with('output.wav', logger=None)
    mock_instance.close.assert_called_once()

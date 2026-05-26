from unittest.mock import patch, MagicMock
from avx.converters.flac_to_wav import convert_flac_to_wav

@patch('avx.converters.flac_to_wav.AudioFileClip')
def test_convert_flac_to_wav(mock_clip):
    """Test flac to wav conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_flac_to_wav('input.flac', 'output.wav')
    mock_clip.assert_called_once_with('input.flac')
    mock_instance.write_audiofile.assert_called_once_with('output.wav', logger=None)
    mock_instance.close.assert_called_once()

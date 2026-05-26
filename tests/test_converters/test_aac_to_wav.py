from unittest.mock import patch, MagicMock
from avx.converters.aac_to_wav import convert_aac_to_wav

@patch('avx.converters.aac_to_wav.AudioFileClip')
def test_convert_aac_to_wav(mock_clip):
    """Test aac to wav conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_aac_to_wav('input.aac', 'output.wav')
    mock_clip.assert_called_once_with('input.aac')
    mock_instance.write_audiofile.assert_called_once_with('output.wav', logger=None)
    mock_instance.close.assert_called_once()

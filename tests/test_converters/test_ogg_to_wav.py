from unittest.mock import patch, MagicMock
from avx.converters.ogg_to_wav import convert_ogg_to_wav

@patch('avx.converters.ogg_to_wav.AudioFileClip')
def test_convert_ogg_to_wav(mock_clip):
    """Test ogg to wav conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_ogg_to_wav('input.ogg', 'output.wav')
    mock_clip.assert_called_once_with('input.ogg')
    mock_instance.write_audiofile.assert_called_once_with('output.wav', logger=None)
    mock_instance.close.assert_called_once()

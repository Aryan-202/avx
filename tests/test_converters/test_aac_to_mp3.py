from unittest.mock import patch, MagicMock
from avx.converters.aac_to_mp3 import convert_aac_to_mp3

@patch('avx.converters.aac_to_mp3.AudioFileClip')
def test_convert_aac_to_mp3(mock_clip):
    """Test aac to mp3 conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_aac_to_mp3('input.aac', 'output.mp3')
    mock_clip.assert_called_once_with('input.aac')
    mock_instance.write_audiofile.assert_called_once_with('output.mp3', logger=None)
    mock_instance.close.assert_called_once()

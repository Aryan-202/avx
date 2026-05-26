from unittest.mock import patch, MagicMock
from avx.converters.mp3_to_aac import convert_mp3_to_aac

@patch('avx.converters.mp3_to_aac.AudioFileClip')
def test_convert_mp3_to_aac(mock_clip):
    """Test mp3 to aac conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mp3_to_aac('input.mp3', 'output.aac')
    mock_clip.assert_called_once_with('input.mp3')
    mock_instance.write_audiofile.assert_called_once_with('output.aac', logger=None)
    mock_instance.close.assert_called_once()

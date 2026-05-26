from unittest.mock import patch, MagicMock
from avx.converters.mp3_to_flac import convert_mp3_to_flac

@patch('avx.converters.mp3_to_flac.AudioFileClip')
def test_convert_mp3_to_flac(mock_clip):
    """Test mp3 to flac conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mp3_to_flac('input.mp3', 'output.flac')
    mock_clip.assert_called_once_with('input.mp3')
    mock_instance.write_audiofile.assert_called_once_with('output.flac', logger=None)
    mock_instance.close.assert_called_once()

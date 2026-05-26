from unittest.mock import patch, MagicMock
from avx.converters.mp3_to_ogg import convert_mp3_to_ogg

@patch('avx.converters.mp3_to_ogg.AudioFileClip')
def test_convert_mp3_to_ogg(mock_clip):
    """Test mp3 to ogg conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mp3_to_ogg('input.mp3', 'output.ogg')
    mock_clip.assert_called_once_with('input.mp3')
    mock_instance.write_audiofile.assert_called_once_with('output.ogg', logger=None)
    mock_instance.close.assert_called_once()

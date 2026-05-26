from unittest.mock import patch, MagicMock
from avx.converters.mp3_to_m4a import convert_mp3_to_m4a

@patch('avx.converters.mp3_to_m4a.AudioFileClip')
def test_convert_mp3_to_m4a(mock_clip):
    """Test mp3 to m4a conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mp3_to_m4a('input.mp3', 'output.m4a')
    mock_clip.assert_called_once_with('input.mp3')
    mock_instance.write_audiofile.assert_called_once_with('output.m4a', logger=None)
    mock_instance.close.assert_called_once()

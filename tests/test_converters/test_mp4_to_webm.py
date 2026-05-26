from unittest.mock import patch, MagicMock
from avx.converters.mp4_to_webm import convert_mp4_to_webm

@patch('avx.converters.mp4_to_webm.VideoFileClip')
def test_convert_mp4_to_webm(mock_clip):
    """Test mp4 to webm conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mp4_to_webm('input.mp4', 'output.webm')
    mock_clip.assert_called_once_with('input.mp4')
    mock_instance.write_videofile.assert_called_once_with('output.webm', logger=None)
    mock_instance.close.assert_called_once()

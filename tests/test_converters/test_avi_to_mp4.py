from unittest.mock import patch, MagicMock
from avx.converters.avi_to_mp4 import convert_avi_to_mp4

@patch('avx.converters.avi_to_mp4.VideoFileClip')
def test_convert_avi_to_mp4(mock_clip):
    """Test avi to mp4 conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_avi_to_mp4('input.avi', 'output.mp4')
    mock_clip.assert_called_once_with('input.avi')
    mock_instance.write_videofile.assert_called_once_with('output.mp4', logger=None)
    mock_instance.close.assert_called_once()

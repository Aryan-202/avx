from unittest.mock import patch, MagicMock
from avx.converters.mkv_to_mp4 import convert_mkv_to_mp4

@patch('avx.converters.mkv_to_mp4.VideoFileClip')
def test_convert_mkv_to_mp4(mock_clip):
    """Test mkv to mp4 conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mkv_to_mp4('input.mkv', 'output.mp4')
    mock_clip.assert_called_once_with('input.mkv')
    mock_instance.write_videofile.assert_called_once_with('output.mp4', logger=None)
    mock_instance.close.assert_called_once()

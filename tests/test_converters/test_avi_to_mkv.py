from unittest.mock import patch, MagicMock
from avx.converters.avi_to_mkv import convert_avi_to_mkv

@patch('avx.converters.avi_to_mkv.VideoFileClip')
def test_convert_avi_to_mkv(mock_clip):
    """Test avi to mkv conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_avi_to_mkv('input.avi', 'output.mkv')
    mock_clip.assert_called_once_with('input.avi')
    mock_instance.write_videofile.assert_called_once_with('output.mkv', logger=None)
    mock_instance.close.assert_called_once()

from unittest.mock import patch, MagicMock
from avx.converters.mkv_to_avi import convert_mkv_to_avi

@patch('avx.converters.mkv_to_avi.VideoFileClip')
def test_convert_mkv_to_avi(mock_clip):
    """Test mkv to avi conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mkv_to_avi('input.mkv', 'output.avi')
    mock_clip.assert_called_once_with('input.mkv')
    mock_instance.write_videofile.assert_called_once_with('output.avi', logger=None)
    mock_instance.close.assert_called_once()

from unittest.mock import patch, MagicMock
from avx.converters.mp4_to_avi import convert_mp4_to_avi

@patch('avx.converters.mp4_to_avi.VideoFileClip')
def test_convert_mp4_to_avi(mock_clip):
    """Test mp4 to avi conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mp4_to_avi('input.mp4', 'output.avi')
    mock_clip.assert_called_once_with('input.mp4')
    mock_instance.write_videofile.assert_called_once_with('output.avi', logger=None)
    mock_instance.close.assert_called_once()

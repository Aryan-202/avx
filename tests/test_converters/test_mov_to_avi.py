from unittest.mock import patch, MagicMock
from avx.converters.mov_to_avi import convert_mov_to_avi

@patch('avx.converters.mov_to_avi.VideoFileClip')
def test_convert_mov_to_avi(mock_clip):
    """Test mov to avi conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mov_to_avi('input.mov', 'output.avi')
    mock_clip.assert_called_once_with('input.mov')
    mock_instance.write_videofile.assert_called_once_with('output.avi', logger=None)
    mock_instance.close.assert_called_once()

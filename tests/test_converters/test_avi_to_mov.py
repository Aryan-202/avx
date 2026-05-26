from unittest.mock import patch, MagicMock
from avx.converters.avi_to_mov import convert_avi_to_mov

@patch('avx.converters.avi_to_mov.VideoFileClip')
def test_convert_avi_to_mov(mock_clip):
    """Test avi to mov conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_avi_to_mov('input.avi', 'output.mov')
    mock_clip.assert_called_once_with('input.avi')
    mock_instance.write_videofile.assert_called_once_with('output.mov', logger=None)
    mock_instance.close.assert_called_once()

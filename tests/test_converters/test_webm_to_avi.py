from unittest.mock import patch, MagicMock
from avx.converters.webm_to_avi import convert_webm_to_avi

@patch('avx.converters.webm_to_avi.VideoFileClip')
def test_convert_webm_to_avi(mock_clip):
    """Test webm to avi conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_webm_to_avi('input.webm', 'output.avi')
    mock_clip.assert_called_once_with('input.webm')
    mock_instance.write_videofile.assert_called_once_with('output.avi', logger=None)
    mock_instance.close.assert_called_once()

from unittest.mock import patch, MagicMock
from avx.converters.webm_to_mp4 import convert_webm_to_mp4

@patch('avx.converters.webm_to_mp4.VideoFileClip')
def test_convert_webm_to_mp4(mock_clip):
    """Test webm to mp4 conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_webm_to_mp4('input.webm', 'output.mp4')
    mock_clip.assert_called_once_with('input.webm')
    mock_instance.write_videofile.assert_called_once_with('output.mp4', logger=None)
    mock_instance.close.assert_called_once()

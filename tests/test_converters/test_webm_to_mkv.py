from unittest.mock import patch, MagicMock
from avx.converters.webm_to_mkv import convert_webm_to_mkv

@patch('avx.converters.webm_to_mkv.VideoFileClip')
def test_convert_webm_to_mkv(mock_clip):
    """Test webm to mkv conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_webm_to_mkv('input.webm', 'output.mkv')
    mock_clip.assert_called_once_with('input.webm')
    mock_instance.write_videofile.assert_called_once_with('output.mkv', logger=None)
    mock_instance.close.assert_called_once()

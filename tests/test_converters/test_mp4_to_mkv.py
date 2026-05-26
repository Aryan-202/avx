from unittest.mock import patch, MagicMock
from avx.converters.mp4_to_mkv import convert_mp4_to_mkv

@patch('avx.converters.mp4_to_mkv.VideoFileClip')
def test_convert_mp4_to_mkv(mock_clip):
    """Test mp4 to mkv conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mp4_to_mkv('input.mp4', 'output.mkv')
    mock_clip.assert_called_once_with('input.mp4')
    mock_instance.write_videofile.assert_called_once_with('output.mkv', logger=None)
    mock_instance.close.assert_called_once()

from unittest.mock import patch, MagicMock
from avx.converters.mov_to_webm import convert_mov_to_webm

@patch('avx.converters.mov_to_webm.VideoFileClip')
def test_convert_mov_to_webm(mock_clip):
    """Test mov to webm conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mov_to_webm('input.mov', 'output.webm')
    mock_clip.assert_called_once_with('input.mov')
    mock_instance.write_videofile.assert_called_once_with('output.webm', logger=None)
    mock_instance.close.assert_called_once()

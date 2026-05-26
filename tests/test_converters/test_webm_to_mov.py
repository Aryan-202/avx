from unittest.mock import patch, MagicMock
from avx.converters.webm_to_mov import convert_webm_to_mov

@patch('avx.converters.webm_to_mov.VideoFileClip')
def test_convert_webm_to_mov(mock_clip):
    """Test webm to mov conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_webm_to_mov('input.webm', 'output.mov')
    mock_clip.assert_called_once_with('input.webm')
    mock_instance.write_videofile.assert_called_once_with('output.mov', logger=None)
    mock_instance.close.assert_called_once()

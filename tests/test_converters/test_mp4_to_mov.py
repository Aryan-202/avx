from unittest.mock import patch, MagicMock
from avx.converters.mp4_to_mov import convert_mp4_to_mov

@patch('avx.converters.mp4_to_mov.VideoFileClip')
def test_convert_mp4_to_mov(mock_clip):
    """Test mp4 to mov conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mp4_to_mov('input.mp4', 'output.mov')
    mock_clip.assert_called_once_with('input.mp4')
    mock_instance.write_videofile.assert_called_once_with('output.mov', logger=None)
    mock_instance.close.assert_called_once()

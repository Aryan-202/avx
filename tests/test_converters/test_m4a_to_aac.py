from unittest.mock import patch, MagicMock
from avx.converters.m4a_to_aac import convert_m4a_to_aac

@patch('avx.converters.m4a_to_aac.AudioFileClip')
def test_convert_m4a_to_aac(mock_clip):
    """Test m4a to aac conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_m4a_to_aac('input.m4a', 'output.aac')
    mock_clip.assert_called_once_with('input.m4a')
    mock_instance.write_audiofile.assert_called_once_with('output.aac', logger=None)
    mock_instance.close.assert_called_once()

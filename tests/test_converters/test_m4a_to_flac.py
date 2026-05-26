from unittest.mock import patch, MagicMock
from avx.converters.m4a_to_flac import convert_m4a_to_flac

@patch('avx.converters.m4a_to_flac.AudioFileClip')
def test_convert_m4a_to_flac(mock_clip):
    """Test m4a to flac conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_m4a_to_flac('input.m4a', 'output.flac')
    mock_clip.assert_called_once_with('input.m4a')
    mock_instance.write_audiofile.assert_called_once_with('output.flac', logger=None)
    mock_instance.close.assert_called_once()

from unittest.mock import patch, MagicMock
from avx.converters.flac_to_aac import convert_flac_to_aac

@patch('avx.converters.flac_to_aac.AudioFileClip')
def test_convert_flac_to_aac(mock_clip):
    """Test flac to aac conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_flac_to_aac('input.flac', 'output.aac')
    mock_clip.assert_called_once_with('input.flac')
    mock_instance.write_audiofile.assert_called_once_with('output.aac', logger=None)
    mock_instance.close.assert_called_once()

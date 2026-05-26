from unittest.mock import patch, MagicMock
from avx.converters.ogg_to_flac import convert_ogg_to_flac

@patch('avx.converters.ogg_to_flac.AudioFileClip')
def test_convert_ogg_to_flac(mock_clip):
    """Test ogg to flac conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_ogg_to_flac('input.ogg', 'output.flac')
    mock_clip.assert_called_once_with('input.ogg')
    mock_instance.write_audiofile.assert_called_once_with('output.flac', logger=None)
    mock_instance.close.assert_called_once()

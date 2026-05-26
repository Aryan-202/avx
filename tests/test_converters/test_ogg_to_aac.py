from unittest.mock import patch, MagicMock
from avx.converters.ogg_to_aac import convert_ogg_to_aac

@patch('avx.converters.ogg_to_aac.AudioFileClip')
def test_convert_ogg_to_aac(mock_clip):
    """Test ogg to aac conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_ogg_to_aac('input.ogg', 'output.aac')
    mock_clip.assert_called_once_with('input.ogg')
    mock_instance.write_audiofile.assert_called_once_with('output.aac', logger=None)
    mock_instance.close.assert_called_once()

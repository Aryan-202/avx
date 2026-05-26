from unittest.mock import patch, MagicMock
from avx.converters.aac_to_m4a import convert_aac_to_m4a

@patch('avx.converters.aac_to_m4a.AudioFileClip')
def test_convert_aac_to_m4a(mock_clip):
    """Test aac to m4a conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_aac_to_m4a('input.aac', 'output.m4a')
    mock_clip.assert_called_once_with('input.aac')
    mock_instance.write_audiofile.assert_called_once_with('output.m4a', logger=None)
    mock_instance.close.assert_called_once()

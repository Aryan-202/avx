from unittest.mock import patch, MagicMock
from avx.converters.m4a_to_ogg import convert_m4a_to_ogg

@patch('avx.converters.m4a_to_ogg.AudioFileClip')
def test_convert_m4a_to_ogg(mock_clip):
    """Test m4a to ogg conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_m4a_to_ogg('input.m4a', 'output.ogg')
    mock_clip.assert_called_once_with('input.m4a')
    mock_instance.write_audiofile.assert_called_once_with('output.ogg', logger=None)
    mock_instance.close.assert_called_once()

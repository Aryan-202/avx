from unittest.mock import patch, MagicMock
from avx.converters.mp3_to_wav import convert_mp3_to_wav

@patch('avx.converters.mp3_to_wav.AudioFileClip')
def test_convert_mp3_to_wav(mock_clip):
    """Test mp3 to wav conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_mp3_to_wav('input.mp3', 'output.wav')
    mock_clip.assert_called_once_with('input.mp3')
    mock_instance.write_audiofile.assert_called_once_with('output.wav', logger=None)
    mock_instance.close.assert_called_once()

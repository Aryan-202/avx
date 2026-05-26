from unittest.mock import patch, MagicMock
from avx.converters.wav_to_flac import convert_wav_to_flac

@patch('avx.converters.wav_to_flac.AudioFileClip')
def test_convert_wav_to_flac(mock_clip):
    """Test wav to flac conversion."""
    mock_instance = MagicMock()
    mock_clip.return_value = mock_instance
    convert_wav_to_flac('input.wav', 'output.flac')
    mock_clip.assert_called_once_with('input.wav')
    mock_instance.write_audiofile.assert_called_once_with('output.flac', logger=None)
    mock_instance.close.assert_called_once()

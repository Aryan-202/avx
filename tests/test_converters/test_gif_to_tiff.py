from unittest.mock import patch, MagicMock
from avx.converters.gif_to_tiff import convert_gif_to_tiff

@patch('avx.converters.gif_to_tiff.Image.open')
def test_convert_gif_to_tiff(mock_open):
    """Test gif to tiff conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_gif_to_tiff('input.gif', 'output.tiff')
    mock_open.assert_called_once_with('input.gif')
    mock_img.save.assert_called_once_with('output.tiff')

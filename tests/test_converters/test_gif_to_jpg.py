from unittest.mock import patch, MagicMock
from avx.converters.gif_to_jpg import convert_gif_to_jpg

@patch('avx.converters.gif_to_jpg.Image.open')
def test_convert_gif_to_jpg(mock_open):
    """Test gif to jpg conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_gif_to_jpg('input.gif', 'output.jpg')
    mock_open.assert_called_once_with('input.gif')
    mock_img.save.assert_called_once_with('output.jpg')

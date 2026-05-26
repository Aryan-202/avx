from unittest.mock import patch, MagicMock
from avx.converters.gif_to_png import convert_gif_to_png

@patch('avx.converters.gif_to_png.Image.open')
def test_convert_gif_to_png(mock_open):
    """Test gif to png conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_gif_to_png('input.gif', 'output.png')
    mock_open.assert_called_once_with('input.gif')
    mock_img.save.assert_called_once_with('output.png')

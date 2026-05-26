from unittest.mock import patch, MagicMock
from avx.converters.gif_to_webp import convert_gif_to_webp

@patch('avx.converters.gif_to_webp.Image.open')
def test_convert_gif_to_webp(mock_open):
    """Test gif to webp conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_gif_to_webp('input.gif', 'output.webp')
    mock_open.assert_called_once_with('input.gif')
    mock_img.save.assert_called_once_with('output.webp')

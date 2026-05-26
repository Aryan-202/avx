from unittest.mock import patch, MagicMock
from avx.converters.gif_to_jpeg import convert_gif_to_jpeg

@patch('avx.converters.gif_to_jpeg.Image.open')
def test_convert_gif_to_jpeg(mock_open):
    """Test gif to jpeg conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_gif_to_jpeg('input.gif', 'output.jpeg')
    mock_open.assert_called_once_with('input.gif')
    mock_img.save.assert_called_once_with('output.jpeg')

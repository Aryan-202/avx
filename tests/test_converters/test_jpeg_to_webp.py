from unittest.mock import patch, MagicMock
from avx.converters.jpeg_to_webp import convert_jpeg_to_webp

@patch('avx.converters.jpeg_to_webp.Image.open')
def test_convert_jpeg_to_webp(mock_open):
    """Test jpeg to webp conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_jpeg_to_webp('input.jpeg', 'output.webp')
    mock_open.assert_called_once_with('input.jpeg')
    mock_img.save.assert_called_once_with('output.webp')

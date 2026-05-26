from unittest.mock import patch, MagicMock
from avx.converters.jpg_to_webp import convert_jpg_to_webp

@patch('avx.converters.jpg_to_webp.Image.open')
def test_convert_jpg_to_webp(mock_open):
    """Test jpg to webp conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_jpg_to_webp('input.jpg', 'output.webp')
    mock_open.assert_called_once_with('input.jpg')
    mock_img.save.assert_called_once_with('output.webp')

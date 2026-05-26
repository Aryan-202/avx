from unittest.mock import patch, MagicMock
from avx.converters.webp_to_jpg import convert_webp_to_jpg

@patch('avx.converters.webp_to_jpg.Image.open')
def test_convert_webp_to_jpg(mock_open):
    """Test webp to jpg conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_webp_to_jpg('input.webp', 'output.jpg')
    mock_open.assert_called_once_with('input.webp')
    mock_img.save.assert_called_once_with('output.jpg')

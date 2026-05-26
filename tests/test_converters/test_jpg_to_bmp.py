from unittest.mock import patch, MagicMock
from avx.converters.jpg_to_bmp import convert_jpg_to_bmp

@patch('avx.converters.jpg_to_bmp.Image.open')
def test_convert_jpg_to_bmp(mock_open):
    """Test jpg to bmp conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_jpg_to_bmp('input.jpg', 'output.bmp')
    mock_open.assert_called_once_with('input.jpg')
    mock_img.save.assert_called_once_with('output.bmp')

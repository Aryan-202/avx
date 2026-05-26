from unittest.mock import patch, MagicMock
from avx.converters.jpeg_to_bmp import convert_jpeg_to_bmp

@patch('avx.converters.jpeg_to_bmp.Image.open')
def test_convert_jpeg_to_bmp(mock_open):
    """Test jpeg to bmp conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_jpeg_to_bmp('input.jpeg', 'output.bmp')
    mock_open.assert_called_once_with('input.jpeg')
    mock_img.save.assert_called_once_with('output.bmp')

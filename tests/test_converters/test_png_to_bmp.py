from unittest.mock import patch, MagicMock
from avx.converters.png_to_bmp import convert_png_to_bmp

@patch('avx.converters.png_to_bmp.Image.open')
def test_convert_png_to_bmp(mock_open):
    """Test png to bmp conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_png_to_bmp('input.png', 'output.bmp')
    mock_open.assert_called_once_with('input.png')
    mock_img.save.assert_called_once_with('output.bmp')

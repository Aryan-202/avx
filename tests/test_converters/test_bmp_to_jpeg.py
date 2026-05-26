from unittest.mock import patch, MagicMock
from avx.converters.bmp_to_jpeg import convert_bmp_to_jpeg

@patch('avx.converters.bmp_to_jpeg.Image.open')
def test_convert_bmp_to_jpeg(mock_open):
    """Test bmp to jpeg conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_bmp_to_jpeg('input.bmp', 'output.jpeg')
    mock_open.assert_called_once_with('input.bmp')
    mock_img.save.assert_called_once_with('output.jpeg')

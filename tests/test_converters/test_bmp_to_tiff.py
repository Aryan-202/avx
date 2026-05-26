from unittest.mock import patch, MagicMock
from avx.converters.bmp_to_tiff import convert_bmp_to_tiff

@patch('avx.converters.bmp_to_tiff.Image.open')
def test_convert_bmp_to_tiff(mock_open):
    """Test bmp to tiff conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_bmp_to_tiff('input.bmp', 'output.tiff')
    mock_open.assert_called_once_with('input.bmp')
    mock_img.save.assert_called_once_with('output.tiff')

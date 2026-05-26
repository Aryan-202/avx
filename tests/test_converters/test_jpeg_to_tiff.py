from unittest.mock import patch, MagicMock
from avx.converters.jpeg_to_tiff import convert_jpeg_to_tiff

@patch('avx.converters.jpeg_to_tiff.Image.open')
def test_convert_jpeg_to_tiff(mock_open):
    """Test jpeg to tiff conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_jpeg_to_tiff('input.jpeg', 'output.tiff')
    mock_open.assert_called_once_with('input.jpeg')
    mock_img.save.assert_called_once_with('output.tiff')

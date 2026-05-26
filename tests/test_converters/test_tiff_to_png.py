from unittest.mock import patch, MagicMock
from avx.converters.tiff_to_png import convert_tiff_to_png

@patch('avx.converters.tiff_to_png.Image.open')
def test_convert_tiff_to_png(mock_open):
    """Test tiff to png conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_tiff_to_png('input.tiff', 'output.png')
    mock_open.assert_called_once_with('input.tiff')
    mock_img.save.assert_called_once_with('output.png')

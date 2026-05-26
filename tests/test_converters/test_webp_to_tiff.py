from unittest.mock import patch, MagicMock
from avx.converters.webp_to_tiff import convert_webp_to_tiff

@patch('avx.converters.webp_to_tiff.Image.open')
def test_convert_webp_to_tiff(mock_open):
    """Test webp to tiff conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_webp_to_tiff('input.webp', 'output.tiff')
    mock_open.assert_called_once_with('input.webp')
    mock_img.save.assert_called_once_with('output.tiff')

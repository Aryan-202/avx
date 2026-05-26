from unittest.mock import patch, MagicMock
from avx.converters.tiff_to_gif import convert_tiff_to_gif

@patch('avx.converters.tiff_to_gif.Image.open')
def test_convert_tiff_to_gif(mock_open):
    """Test tiff to gif conversion."""
    mock_img = MagicMock()
    mock_img.mode = 'RGB'
    mock_open.return_value.__enter__.return_value = mock_img
    convert_tiff_to_gif('input.tiff', 'output.gif')
    mock_open.assert_called_once_with('input.tiff')
    mock_img.save.assert_called_once_with('output.gif')

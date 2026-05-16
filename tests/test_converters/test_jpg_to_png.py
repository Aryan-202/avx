from unittest.mock import patch, MagicMock
from avx.converters.jpg_to_png import convert_jpg_to_png

@patch('avx.converters.jpg_to_png.Image.open')
def test_convert_jpg_to_png_success(mock_open):
    """Test that jpg to png conversion opens the file and saves correctly."""
    mock_img = MagicMock()
    # Handle context manager
    mock_open.return_value.__enter__.return_value = mock_img
    
    convert_jpg_to_png('input.jpg', 'output.png')
    
    mock_open.assert_called_once_with('input.jpg')
    mock_img.save.assert_called_once_with('output.png')

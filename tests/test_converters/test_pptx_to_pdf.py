import os
from unittest.mock import patch, MagicMock
from avx.converters.pptx_to_pdf import convert_pptx_to_pdf

@patch('comtypes.client.CreateObject')
def test_convert_pptx_to_pdf_success(mock_create_object):
    """Test that pptx to pdf conversion automates PowerPoint correctly."""
    
    # Mock the COM objects
    mock_powerpoint = MagicMock()
    mock_create_object.return_value = mock_powerpoint
    
    mock_deck = MagicMock()
    mock_powerpoint.Presentations.Open.return_value = mock_deck
    
    input_path = 'input.pptx'
    output_path = 'output.pdf'
    
    convert_pptx_to_pdf(input_path, output_path)
    
    # Verify the COM application was created
    mock_create_object.assert_called_once_with("Powerpoint.Application")
    
    # Verify the deck was opened with absolute path
    mock_powerpoint.Presentations.Open.assert_called_once_with(os.path.abspath(input_path))
    
    # Verify the deck was saved as PDF (format 32)
    mock_deck.SaveAs.assert_called_once_with(os.path.abspath(output_path), 32)
    
    # Verify cleanup
    mock_deck.Close.assert_called_once()
    mock_powerpoint.Quit.assert_called_once()

from unittest.mock import patch
from avx.converters.docx_to_pdf import convert_docx_to_pdf

@patch('avx.converters.docx_to_pdf.convert')
def test_convert_docx_to_pdf_success(mock_convert):
    """Test that docx to pdf conversion calls the underlying library correctly."""
    
    convert_docx_to_pdf('input.docx', 'output.pdf')
    
    mock_convert.assert_called_once_with(input_path='input.docx', output_path='output.pdf')

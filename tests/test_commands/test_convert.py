from unittest.mock import patch
from avx.commands.convert import convert_files

class TestConvertFiles:
    @patch('avx.commands.convert.console.print')
    @patch('glob.glob')
    def test_convert_nonexistent_file(self, mock_glob, mock_print):
        """Test conversion of a non-existent file."""
        mock_glob.return_value = []
        convert_files("nonexistent.pdf", "output.txt")
        
        mock_print.assert_called_once()
        args, _ = mock_print.call_args
        assert "No files found matching" in args[0]

    @patch('glob.glob')
    @patch('os.path.isfile')
    @patch('avx.converters.convert_docx_to_pdf')
    def test_convert_docx_to_pdf(self, mock_convert, mock_isfile, mock_glob):
        """Test DOCX to PDF conversion."""
        mock_glob.return_value = ["test.docx"]
        mock_isfile.return_value = True
        convert_files("test.docx", "test.pdf")
        mock_convert.assert_called_once_with("test.docx", "test.pdf")

    @patch('glob.glob')
    @patch('os.path.isfile')
    @patch('avx.converters.convert_pptx_to_pdf')
    def test_convert_pptx_to_pdf(self, mock_convert, mock_isfile, mock_glob):
        """Test PPTX to PDF conversion."""
        mock_glob.return_value = ["test.pptx"]
        mock_isfile.return_value = True
        convert_files("test.pptx", "test.pdf")
        mock_convert.assert_called_once_with("test.pptx", "test.pdf")

    @patch('glob.glob')
    @patch('os.path.isfile')
    @patch('avx.converters.convert_jpg_to_png')
    def test_convert_jpg_to_png(self, mock_convert, mock_isfile, mock_glob):
        """Test JPG to PNG conversion."""
        mock_glob.return_value = ["test.jpg"]
        mock_isfile.return_value = True
        convert_files("test.jpg", "test.png")
        mock_convert.assert_called_once_with("test.jpg", "test.png")

    @patch('glob.glob')
    @patch('os.path.isfile')
    @patch('avx.commands.convert.console.print')
    def test_unsupported_conversion(self, mock_print, mock_isfile, mock_glob):
        """Test conversion with unsupported extensions."""
        mock_glob.return_value = ["test.unknown"]
        mock_isfile.return_value = True
        convert_files("test.unknown", "test.pdf")
        
        mock_print.assert_called_once()
        args, _ = mock_print.call_args
        assert "Unsupported extensions" in args[0] or "not supported" in args[0] or "Domains must match" in args[0]

    @patch('glob.glob')
    @patch('os.path.isfile')
    @patch('avx.commands.convert.console.print')
    def test_cross_domain_conversion(self, mock_print, mock_isfile, mock_glob):
        """Test conversion between different domains (should fail)."""
        mock_glob.return_value = ["test.docx"]
        mock_isfile.return_value = True
        convert_files("test.docx", "test.png")
        
        mock_print.assert_called_once()
        args, _ = mock_print.call_args
        assert "Cross-Domain Error" in args[0]
from unittest.mock import patch
from avx.commands.convert import convert_files
import argparse

class TestConvertFiles:
    @patch('os.path.exists')
    def test_convert_nonexistent_file(self, mock_exists, capsys):
        """Test conversion with non-existent input file."""
        mock_exists.return_value = False
        args = argparse.Namespace(
            input="nonexistent.docx",
            output="output.pdf"
        )
        convert_files(args)
        captured = capsys.readouterr()
        assert "file does not exists" in captured.out

    @patch('os.path.exists')
    @patch('avx.converters.convert_docx_to_pdf')
    def test_convert_docx_to_pdf(self, mock_convert, mock_exists):
        """Test DOCX to PDF conversion."""
        mock_exists.return_value = True
        args = argparse.Namespace(
            input="test.docx",
            output="test.pdf"
        )
        convert_files(args)
        mock_convert.assert_called_once_with("test.docx", "test.pdf")

    @patch('os.path.exists')
    @patch('avx.converters.convert_pptx_to_pdf')
    def test_convert_pptx_to_pdf(self, mock_convert, mock_exists):
        """Test PPTX to PDF conversion."""
        mock_exists.return_value = True
        args = argparse.Namespace(
            input="test.pptx",
            output="test.pdf"
        )
        convert_files(args)
        mock_convert.assert_called_once_with(
            input_path="test.pptx",
            output_path="test.pdf"
        )

    @patch('os.path.exists')
    @patch('avx.converters.convert_jpg_to_png')
    def test_convert_jpg_to_png(self, mock_convert, mock_exists):
        """Test JPG to PNG conversion."""
        mock_exists.return_value = True
        args = argparse.Namespace(
            input="test.jpg",
            output="test.png"
        )
        convert_files(args)
        mock_convert.assert_called_once_with("test.jpg", "test.png")

    @patch('os.path.exists')
    def test_unsupported_conversion(self, mock_exists, capsys):
        """Test unsupported conversion format."""
        mock_exists.return_value = True
        args = argparse.Namespace(
            input="test.txt",
            output="test.pdf"
        )
        convert_files(args)
        captured = capsys.readouterr()
        assert "conversion not supported" in captured.out
import unittest
import argparse
from unittest.mock import patch

from avx.commands.convert import convert_files


class TestDocxToPdf(unittest.TestCase):
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

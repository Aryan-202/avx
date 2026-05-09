import pytest
from unittest.mock import patch, MagicMock
import sys
from avx.cli import main

class TestCLI:
    def test_main_no_args(self, capsys):
        """Test CLI with no arguments shows help."""
        test_args = ["avx"]
        with patch.object(sys, 'argv', test_args):
            main()
        captured = capsys.readouterr()
        assert "usage:" in captured.out or "usage:" in captured.err

    @patch('avx.cli.list_files')
    def test_ls_command(self, mock_list_files):
        """Test ls command calls list_files."""
        test_args = ["avx", "ls"]
        with patch.object(sys, 'argv', test_args):
            main()
        mock_list_files.assert_called_once()

    @patch('avx.cli.list_files')
    def test_ls_with_all_flag(self, mock_list_files):
        """Test ls command with -a flag."""
        test_args = ["avx", "ls", "-a"]
        with patch.object(sys, 'argv', test_args):
            main()
        mock_list_files.assert_called_once()
        # Verify the args object has all=True
        call_args = mock_list_files.call_args[0][0]
        assert call_args.all == True

    @patch('avx.cli.convert_files')
    def test_convert_command(self, mock_convert_files):
        """Test convert command calls convert_files."""
        test_args = ["avx", "convert", "input.docx", "-o", "output.pdf"]
        with patch.object(sys, 'argv', test_args):
            main()
        mock_convert_files.assert_called_once()
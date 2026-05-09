import pytest
from unittest.mock import patch, MagicMock
from avx.commands.ls import list_files
import argparse

class TestListFiles:
    @patch('avx.commands.ls.console')
    def test_list_files_normal(self, mock_console, sample_files):
        """Test listing files without hidden files."""
        args = argparse.Namespace(all=False)
        list_files(args)
        mock_console.print.assert_called_once()

    @patch('avx.commands.ls.console')
    def test_list_files_with_hidden(self, mock_console, sample_files):
        """Test listing files including hidden files."""
        args = argparse.Namespace(all=True)
        list_files(args)
        mock_console.print.assert_called_once()

    @patch('avx.commands.ls.os.listdir')
    @patch('avx.commands.ls.console')
    def test_list_files_empty_directory(self, mock_console, mock_listdir):
        """Test listing files in empty directory."""
        mock_listdir.return_value = []
        args = argparse.Namespace(all=False)
        list_files(args)
        mock_console.print.assert_called_once()
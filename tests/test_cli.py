import pytest
from unittest.mock import patch
from typer.testing import CliRunner
from avx.cli import app

runner = CliRunner()

class TestCLI:
    def test_main_no_args(self):
        """Test CLI with no arguments shows help."""
        result = runner.invoke(app, [])
        assert result.exit_code != 0
        assert "Missing argument" in result.output or "Usage:" in result.output

    @patch('avx.cli.list_files')
    def test_ls_command(self, mock_list_files):
        """Test ls command calls list_files."""
        result = runner.invoke(app, ["ls"])
        mock_list_files.assert_called_once_with(False)
        assert result.exit_code == 0

    @patch('avx.cli.list_files')
    def test_ls_with_all_flag(self, mock_list_files):
        """Test ls command with -a flag."""
        result = runner.invoke(app, ["ls", "-a"])
        mock_list_files.assert_called_once_with(True)
        assert result.exit_code == 0

    @patch('avx.cli.convert_files')
    def test_convert_command(self, mock_convert_files):
        """Test convert command calls convert_files."""
        result = runner.invoke(app, ["convert", "input.docx", "-o", "output.pdf"])
        mock_convert_files.assert_called_once_with("input.docx", "output.pdf")
        assert result.exit_code == 0
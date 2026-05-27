import unittest
from unittest.mock import patch
from avx.commands.ls import list_files
import argparse

class TestLs(unittest.TestCase):
    @patch('avx.commands.ls.os.listdir')
    @patch('avx.commands.ls.os.path.isdir')
    @patch('avx.commands.ls.os.path.isfile')
    @patch('avx.commands.ls.os.path.getsize')
    @patch('avx.commands.ls.os.path.getmtime')
    @patch('avx.commands.ls.console.print')
    def test_list_files(self, mock_print, mock_getmtime, mock_getsize, mock_isfile, mock_isdir, mock_listdir):
        # Setup mock data
        mock_listdir.return_value = ['file1.txt', 'dir1', '.hidden']
        mock_isdir.return_value = False
        mock_isfile.return_value = True
        mock_getsize.return_value = 1024
        mock_getmtime.return_value = 1600000000.0
        
        args = argparse.Namespace(all=False)
        
        # Run function
        list_files(args)
        
        # Verify it printed the table
        mock_print.assert_called_once()
        self.assertTrue(True)
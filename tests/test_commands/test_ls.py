import unittest
from unittest.mock import patch, MagicMock
from avx.commands.ls import list_files
import argparse

class TestLs(unittest.TestCase):
    def setUp(self):
        pass

    @patch('avx.commands.convert.convert_files.list_files')
    def test_list_files(self, list_files_mock):
        list_files_mock.return_value = [

        ]
import argparse
import os
import sys
import unittest
from unittest.mock import patch


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from run_synchronizer import RunSynchronizer


class TestRunSynchronizer(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(source_path='/path/to/source',
                                           target_path='/path/to/target', interval=3600))
    def test_get_args_from_command_line(self, mock_parse_args):
        expected_args = {
            'source_path': '/path/to/source',
            'target_path': '/path/to/target',
            'interval': 3600
        }
        actual_args = RunSynchronizer.get_args_from_command_line()
        self.assertDictEqual(vars(actual_args), expected_args)

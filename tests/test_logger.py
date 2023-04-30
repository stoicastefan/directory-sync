import os
import re
import sys
import unittest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logger import Logger


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def test_create_info_log(self):
        message = 'Test message'
        self.logger.create_info_log(message)

        file = open('log_file.log')
        lines = file.read().splitlines()
        file.close()
        last_line_in_log_file = lines[-1]

        is_correct = re.match('....................... \[INFO\] Test message', last_line_in_log_file)
        self.assertIsNot(is_correct, None)


if __name__ == '__main__':
    unittest.main()




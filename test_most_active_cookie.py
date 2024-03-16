import unittest
from unittest.mock import patch
from io import StringIO
import sys

from most_active_cookie import fetchCookiesAsPerDate, getMostActiveCookies, main

class TestCookieFunctions(unittest.TestCase):

    #Setting up units tests
    def setUp(self):
        self.file_content = [
            "cookie1,2023-05-01T10:00:00+00:00\n",
            "cookie2,2023-05-01T10:05:00+00:00\n",
            "cookie1,2023-05-01T10:10:00+00:00\n",
            "cookie2,2023-05-02T10:00:00+00:00\n",
            "cookie3,2023-05-02T10:05:00+00:00\n"
        ]
        self.fetched_cookies = {
            '2023-05-01': {'cookie1': 2, 'cookie2': 1},
            '2023-05-02': {'cookie2': 1, 'cookie3': 1}
        }

        #Patching builtins.open
        self.mock_open = patch('builtins.open', return_value=StringIO(
            "cookie1,2023-05-01T10:00:00+00:00\n"
            "cookie2,2023-05-01T10:05:00+00:00\n"
            "cookie1,2023-05-01T10:10:00+00:00\n"
            "cookie2,2023-05-02T10:00:00+00:00\n"
            "cookie3,2023-05-02T10:05:00+00:00\n"
        )).start()

    #Tearing down the unit tests
    def tearDown(self):
        self.mock_open.stop()

    #Tests fetchCookiesAsPerDate func
    def test_fetchCookiesAsPerDate(self):
        expected_output = {
            '2023-05-01': {'cookie1': 2, 'cookie2': 1},
            '2023-05-02': {'cookie2': 1, 'cookie3': 1}
        }
        result = fetchCookiesAsPerDate(self.file_content)
        self.assertEqual(result, expected_output)

    #Tests getMostActiveCookies func
    def test_getMostActiveCookies(self):
        result = getMostActiveCookies(self.fetched_cookies, '2023-05-01')
        self.assertEqual(result, ['cookie1'])

    #Tests getMostActiveCookies func when multiple most active cookies exists for the same date
    def test_getMostActiveCookiesWhenMutipleMostActiveCookiesExists(self):
        result = getMostActiveCookies(self.fetched_cookies, '2023-05-02')
        self.assertEqual(result, ['cookie2', 'cookie3'])
    
    #Tests main func 
    @patch('sys.stdout', new_callable=StringIO)
    def test_mainSuccess(self, mock_stdout):
        sys.argv = ['assignment.py', 'test.csv', '-d', '2023-05-01']
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), 'cookie1')

    #Tests main func when the entered date doesn't exists in the log
    @patch('sys.stdout', new_callable=StringIO)
    def test_mainWhenDateIsInvalid(self, mock_stdout):
        sys.argv = ['assignment.py', 'test.csv', '-d', '2023-05-11']
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), 'No such date exists in the log')

if __name__ == '__main__':
    unittest.main()

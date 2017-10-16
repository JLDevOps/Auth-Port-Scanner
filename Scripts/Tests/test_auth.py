import unittest
from random import randint

from mock import patch

from Scripts.auth_port_scanner import *


class test_auth(unittest.TestCase):
    def test_scrape(self):
        file_path = 'Test_Logs/test.log'
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, file_path)
        ipDict = auth_scrape(filename)
        sizeDict = get_size_dict(ipDict)
        if (sizeDict == 0):
            assert False, "test_scrape Failed: Dictionary does not contain any results"

        assert True, "test_scrape Successful"

    def test_prompt(self):
        rand_option = randint(1, 4)
        try:
            with patch('__builtin__.raw_input', return_value=str(rand_option)) as raw_input:
                assert True, "test_prompt Successful"
        except:
            assert False, "test_prompt Failed: Choices are unreadable"

    def test_individual_port(self):
        with patch('__builtin__.raw_input', side_effect=['1', '']) as _raw_input:
            prompt()

if __name__ == '__main__':
    unittest.main()

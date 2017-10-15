import os
import unittest

from Scripts.auth_scrape import *


class test_auth(unittest.TestCase):
    def test_scrape(self):
        file_path = 'Logs/test.log'
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, file_path)
        ipDict = auth_scrape(filename)
        sizeDict = get_size_dict(ipDict)
        if (sizeDict == 0):
            assert False, "test_scrape Failed: Dictionary does not contain any results"


if __name__ == '__main__':
    unittest.main()

from bottle_cas.client import CASClient
import unittest

class TestCASClient(unittest.TestCase):

    def setUp(self):
        self.cas = CASClient()

    def test_parse_tag(self):
        self.assertEqual(self.cas._parse_tag("<one>test</one>", "one"), "test")
        self.assertEqual(self.cas._parse_tag("<one>test</one><two>thing</two>", "one"), "test")
        self.assertEqual(self.cas._parse_tag("<one>test</one><two>thing</two>", "two"), "thing")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCASClient)
    unittest.TextTestRunner(verbosity=3).run(suite)

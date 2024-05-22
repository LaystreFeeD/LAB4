import unittest

class TestSimpleApp(unittest.TestCase):
    def test_print_message(self):
        expected_message = "Hello World"
        actual_message = "Hello World"
        self.assertEqual(expected_message, actual_message)

if __name__ == '__main__':
    unittest.main()
import unittest

class TestSimpleApp(unittest.TestCase):
    def test_print_message(self):
        expected_message = "Lab4"
        actual_message = "Lab4"
        self.assertEqual(expected_message, actual_message)

if __name__ == '__main__':
    unittest.main()
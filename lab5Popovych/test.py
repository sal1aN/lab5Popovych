import unittest
from unittest.mock import patch

from lab5Popovych.main import validateString, ValidationError

class Test(unittest.TestCase):
    def test_validateString(self):
        valid_cases = [
            "",
            "Hello World",
            "()",
            "{[(<>)]}",
            "<div><p>{ test }</p></div>"
        ]
        for case in valid_cases:
            with self.subTest(case=case):
                self.assertTrue(validateString(case))

    @patch('sys.stderr')
    def test_example_task(self, mock_stderr):
        case = "<div><p>{ test }}</p</div>"
        with self.assertRaises(ValidationError) as context:
            validateString(case)
        self.assertEqual(context.exception.index, [16, 17])
        self.assertIn("at 16, at 17", str(context.exception))

    @patch('sys.stderr')
    def test_unclosed_brackets(self, mock_stderr):
        case = "{[(<"
        with self.assertRaises(ValidationError) as context:
            validateString(case)
        self.assertEqual(context.exception.index, [0, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()
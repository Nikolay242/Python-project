import unittest
from io import StringIO
import sys
from src.brainfuck_utils import BrainfuckUtils
from src.brainfuck_exceptions import (
    MemoryOverflowError,
    MemoryUnderflowError,
    MemoryOutOfBoundsError,
    UnmatchedBracketError,
    PossibleInfiniteLoopError,
    InputError
)

MAX_LOOP_ITERATIONS = 2_147_483_646
class TestBrainfuckUtils(unittest.TestCase):
    def setUp(self):
        self.utils = BrainfuckUtils()

    def test_clean_valid_chars(self):
        self.assertEqual(self.utils.clean("++--.,<>[]ABC"), "++--.,<>[]")

    def test_clean_empty(self):
        self.assertEqual(self.utils.clean(""), "")

    def test_match_brackets_valid(self):
        self.assertEqual(self.utils.match_brackets("[]"), {0: 1, 1: 0})
        self.assertEqual(self.utils.match_brackets("[[[]]]"), {0: 5, 5: 0, 1: 4, 4: 1, 2: 3, 3: 2})
        self.assertEqual(self.utils.match_brackets("++[->+<]"), {2: 7, 7: 2})

    def test_match_brackets_unmatched_closing(self):
        with self.assertRaises(UnmatchedBracketError):
            self.utils.match_brackets("][")

    def test_match_brackets_unmatched_opening(self):
        with self.assertRaises(UnmatchedBracketError):
            self.utils.match_brackets("[[]")

    def test_state_memory_overflow(self):
        utils = BrainfuckUtils(wrap_around=False)
        with self.assertRaises(MemoryOverflowError):
            utils.state("+", [255], 0, 0, {}, {})

    def test_state_memory_underflow(self):
        utils = BrainfuckUtils(wrap_around=False)
        with self.assertRaises(MemoryUnderflowError):
            utils.state("-", [0], 0, 0, {}, {})

    def test_state_out_of_bounds_left(self):
        with self.assertRaises(MemoryOutOfBoundsError):
            self.utils.state("<", [0], 0, 0, {}, {})

    def test_state_input_error(self):
        self.utils = BrainfuckUtils()
        sys.stdin = StringIO('AB')
        with self.assertRaises(InputError):
            self.utils.state(",", [0], 0, 0, {}, {})



if __name__ == "__main__":
    unittest.main()

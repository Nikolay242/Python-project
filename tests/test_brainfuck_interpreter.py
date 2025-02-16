import unittest
from io import StringIO
import sys
from src.brainfuck_interpreter import BrainfuckInterpreter

class TestBrainfuckInterpreter(unittest.TestCase):
    
    def setUp(self):
        self.interpreter = None

    def test_increment_cell(self):
        self.interpreter = BrainfuckInterpreter("+")
        self.interpreter.run()
        self.assertEqual(self.interpreter.state("+", [0], 0, 0, {}, {})[0][0], 1)

    def test_decrement_cell(self):
        self.interpreter = BrainfuckInterpreter("-")
        self.interpreter.run()
        self.assertEqual(self.interpreter.state("-", [1], 0, 0, {}, {})[0][0], 0)

    def test_move_pointer_right(self):
        self.interpreter = BrainfuckInterpreter(">")
        self.interpreter.run()
        self.assertEqual(self.interpreter.state(">", [0], 0, 0, {}, {})[1], 1)

    def test_move_pointer_left(self):
        self.interpreter = BrainfuckInterpreter("<")
        with self.assertRaises(Exception):
            self.interpreter.run()

    def test_loop_execution(self):
        self.interpreter = BrainfuckInterpreter("+++[->+<]>.")
        output = self.capture_output(self.interpreter.run)
        self.assertEqual(output, "\x03")

    def test_output_character(self):
        self.interpreter = BrainfuckInterpreter("++++++++++[>++++++++<-]>.")
        output = self.capture_output(self.interpreter.run)
        self.assertEqual(output, "P")

    def test_input_character(self):
        self.interpreter = BrainfuckInterpreter(",.")
        sys.stdin = StringIO('A')  
        output = self.capture_output(self.interpreter.run)
        output = output.replace("Enter one character: ", "").strip()
        self.assertEqual(output, 'A')


    def capture_output(self, func):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        func()
        output = sys.stdout.getvalue().strip()
        sys.stdout = old_stdout
        return output

if __name__ == '__main__':
    unittest.main()

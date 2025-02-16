import unittest
from src.brainfuck_debugger import BrainfuckDebugger

class TestBrainfuckDebugger(unittest.TestCase):

    def setUp(self):
        self.debugger = BrainfuckDebugger("++>++<[->+<]>.")

    def test_initial_state(self):
        self.assertEqual(self.debugger.ptr, 0)
        self.assertEqual(self.debugger.cellptr, 0)
        self.assertEqual(self.debugger.cells, [0])

    def test_step_forward(self):
        self.debugger.step_forward()
        self.assertEqual(self.debugger.ptr, 1)
        self.assertEqual(self.debugger.cells[0], 1)

    def test_step_backward(self):
        self.debugger.step_forward()
        self.debugger.step_forward()
        self.debugger.step_backward()
        self.assertEqual(self.debugger.ptr, 1)
        self.assertEqual(self.debugger.cells[0], 1)

    def test_skip_forward(self):
        self.debugger.skip_instructions("5s")
        self.assertEqual(self.debugger.ptr, 5)

    def test_skip_backward(self):
        self.debugger.skip_instructions("5s")
        self.debugger.skip_instructions("2b")
        self.assertEqual(self.debugger.ptr, 3)

    def test_print_memory(self):
        try:
            self.debugger.print_memory()
        except Exception as e:
            self.fail(f"print_memory() хвърли грешка: {e}")

    def test_print_program_context(self):
        try:
            self.debugger.print_program_context()
        except Exception as e:
            self.fail(f"print_program_context() хвърли грешка: {e}")

    def test_run_debug_quit(self):
        from unittest.mock import patch

        with patch("builtins.input", side_effect=["q"]):
            try:
                self.debugger.run_debug()
            except Exception as e:
                self.fail(f"run_debug() хвърли грешка: {e}")

if __name__ == "__main__":
    unittest.main()

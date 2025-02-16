"""
This module is for the interpreter
"""
from src.brainfuck_utils import BrainfuckUtils

class BrainfuckInterpreter(BrainfuckUtils):
    def __init__(self, program: str, cell_size = 255, wrap_around = True):
        super().__init__(cell_size, wrap_around)
        self.program = self.clean(list(program))
        self.brackets = self.match_brackets(self.program)

    def run(self) -> None:
        """
        This is the main function that interpreta the code
        """
        cells, cellptr, ptr = [0], 0, 0

        while ptr < len(self.program):
            command = self.program[ptr]
            cells, cellptr, ptr = self.state(command, cells, cellptr, ptr, self.brackets)
            ptr += 1

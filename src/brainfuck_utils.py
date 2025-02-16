"""
This module is for the utils you are going to reuse in interpreter and the debugger
"""
import sys
from src.brainfuck_exceptions import (
    MemoryOverflowError,
    MemoryUnderflowError,
    MemoryOutOfBoundsError,
    UnmatchedBracketError,
    InputError
)

class BrainfuckUtils:
    def __init__(self, cell_size = 255, wrap_around = True):
        self.cell_size = cell_size
        self.wrap_around = wrap_around

    def state(self, command, cells, cellptr, ptr, brackets):
        """
        This function return the state of the program
        """
        if command == "+":
            if self.wrap_around:
                cells[cellptr] = (cells[cellptr] + 1) % (self.cell_size + 1)
            elif cells[cellptr] >= self.cell_size:
                raise MemoryOverflowError(cellptr, cells[cellptr] + 1)
            else:
                cells[cellptr] += 1

        elif command == "-":
            if self.wrap_around:
                cells[cellptr] = (cells[cellptr] - 1) % (self.cell_size + 1)
            elif cells[cellptr] <= 0:
                raise MemoryUnderflowError(cellptr, cells[cellptr] - 1)
            else:
                cells[cellptr] -= 1

        elif command == ">":
            cellptr += 1
            if cellptr == len(cells):
                cells.append(0)

        elif command == "<":
            if cellptr == 0:
                raise MemoryOutOfBoundsError(cellptr - 1, len(cells))
            cellptr -= 1

        elif command == ".":
            sys.stdout.write(chr(cells[cellptr]))
            sys.stdout.flush()

        elif command == ",":
            user_input = input("Enter one character: ")
            if len(user_input) != 1:
                raise InputError(user_input)
            cells[cellptr] = ord(user_input)

        elif command == "[":
            if cells[cellptr] == 0:
                ptr = brackets[ptr]

        elif command == "]":
            if cells[cellptr] != 0:
                ptr = brackets[ptr] - 1

        return cells, cellptr, ptr

    def match_brackets(self, commands):
        """
        This function makes dict for the brackets possitions after the commands are cleaned 
        from symbols that are not in the language.
        """
        stack, brackets = [], {}

        for pos, el in enumerate(commands):
            if el == "[":
                stack.append(pos)
            elif el == "]":
                if not stack:
                    raise UnmatchedBracketError(pos, "]")
                start = stack.pop()
                brackets[start] = pos
                brackets[pos] = start

        if stack:
            raise UnmatchedBracketError(stack.pop(), "[")
    
        return brackets
    
    def clean(self, lst):
        """
        This function cleans the commands before the debugging/interpreting even starts
        """
        return "".join(filter (lambda x : x in {",", ".", "+", "-", "[", "]", ">", "<"}, lst))



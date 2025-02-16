"""
This module is for possible exceptions when you interpretate or dedub
"""
class BrainfuckError(Exception):
    pass

class MemoryOverflowError(BrainfuckError):
    def __init__(self, pointer: int, value: int):
        super().__init__(f"Error: Memory overflow at cell {pointer}: attempted to set value {value}")

class MemoryUnderflowError(BrainfuckError):
    def __init__(self, pointer: int, value: int):
        super().__init__(f"Error: Memory underflow at cell {pointer}: attempted to set value {value}")

class MemoryOutOfBoundsError(BrainfuckError):
    def __init__(self, pointer: int, memory_size: int):
        super().__init__(f"Error: Memory pointer out of bounds: {pointer}. Allowed range: 0 to {memory_size - 1}.")

class UnmatchedBracketError(BrainfuckError):
    def __init__(self, position: int, bracket_type: str):
        super().__init__(f"Error: Unmatched '{bracket_type}' bracket at position {position}.")

class DebuggerStopError(BrainfuckError):
    def __init__(self):
        super().__init__("Error: Debugger manually stopped.")

class InputError(BrainfuckError):
    def __init__(self, input_data: str):
        super().__init__(f"Error: Invalid input data '{input_data}': Command ',' expects exactly one character.")




"""
This module is for the debugger
"""

from src.brainfuck_utils import BrainfuckUtils
from colorama import Fore, Style
import sys

class BrainfuckDebugger(BrainfuckUtils):
    def __init__(self, program: str, cell_size = 255, wrap_around = True):
        super().__init__(cell_size, wrap_around)
        self.program = self.clean(list(program))
        self.brackets = self.match_brackets(self.program)
        self.cells, self.cellptr, self.ptr = [0] , 0 , 0
        self.history = []

    def step_forward(self) -> bool:
        """
        Function for goint to the next operation
        """
        if self.ptr >= len(self.program):
                print("\nEnd of program.")
                sys.stdout.flush()
                return True

        command = self.program[self.ptr]
            
        self.history.append((self.cells[:], self.cellptr, self.ptr))
        self.cells, self.cellptr, self.ptr = self.state(command, self.cells, self.cellptr, self.ptr, self.brackets)

        self.ptr += 1

        return False

    def step_backward(self) -> bool:
        """
        Function used for goint to the prev operation
        """
        if self.history:
            self.cells, self.cellptr, self.ptr = self.history.pop()
        else:
            print("\nNo previous state to revert to.")
            return True
        
        return False

    def print_memory(self) -> None:
        """
        Printing the memory blocks to show what is happening
        """
        end = self.cellptr + 10
        memory_view = "\nMemory State:\n"

        memory_view += " ".join(
            f"{Fore.BLUE}[{Fore.GREEN}{self.cells[i] if i < len(self.cells) else 0}{Fore.BLUE}]{Style.RESET_ALL}"
            if i == self.cellptr else
            f"[{self.cells[i] if i < len(self.cells) else 0}]"
            for i in range(end)
        )

        print(memory_view + "\n")


    def print_program_context(self) -> None:
        """
        Pointer for the current operation
        """
        start = max(0, self.ptr - 3)
        end = min(len(self.program), self.ptr + 4)
        snippet = "".join(self.program[start:end])

        pointer_position = self.ptr - start
        arrow_line = " " * pointer_position + "^"

        print("\nCurrent Operation:")
        print(snippet)
        print(arrow_line + "\n")

    def skip_instructions(self, command: str) ->bool:
        """
        Function for skipping more than 1 step
        """
        num_steps = int(command[:-1]) if command[:-1].isdigit() else 1
        action = command[-1]
        no_more_steps = False

        for _ in range(num_steps):
            if action == 's':
                if self.step_forward():
                    return True
            elif action == 'b':
                no_more_steps = self.step_backward()
            else:
                print("Invalid skip command. Use format like '10s' or '5b'.")
                break 
            if no_more_steps: break
        
        return False
    def run_debug(self) ->None:
        """
        Core funtion for debug
        """
        print("Brainfuck Debugger Started. Controls: [s] Step Forward, [b] Step Back, [m] Show Memory, [q] quit")
        running = False
        while not running:
            self.print_program_context()
            command = input("Enter: ").strip().lower()

            if command == 's':  
                running = self.step_forward()
            elif command == 'b':  
                self.step_backward()
            elif command == "m":
                self.print_memory()
            elif command == 'q':  
                print("Quit debugger.")
                break
            elif command[:-1].isdigit() and command[-1] in {'s', 'b'}:
                running = self.skip_instructions(command)

            else:
                print("Invalid command. Use 's', 'b', 'q'.")



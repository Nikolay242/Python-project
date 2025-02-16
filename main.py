import argparse
import sys
from src.brainfuck_interpreter import BrainfuckInterpreter
from src.brainfuck_debugger import BrainfuckDebugger

"""
    Main module.
    Example for using
    python main.py r
    python main.py r --f --cell-size 16
    python main.py r --f <some file name> --cell-size 16
"""
def parse_args():
    parser = argparse.ArgumentParser(description="Brainfuck Interpreter & Debugger")
    
    parser.add_argument(
        "action", choices=["r", "run", "d", "debug"], 
        help="Choose r/run for executing a program or d/debug for debugging a program"
    )

    parser.add_argument(
        "--f", "--file", dest="file", 
        help="Path to an executable or debug file"
    )

    parser.add_argument(
        "--cell-size", type=int, choices=[8, 16, 32, 64], default=8, 
        help="Cell size in bits (default: 8-bit)"
    )

    parser.add_argument(
        "--no-wrap", action="store_true", 
        help="Turns off wrap-around (overflow and subzero values throw an error)"
    )

    return parser.parse_args()

def main():
    args = parse_args()

    CELL_MAX = (2 ** args.cell_size) - 1
    WRAP_AROUND = not args.no_wrap

    if args.action in ["r", "run"]:
        run_brainfuck(args.file, CELL_MAX, WRAP_AROUND)
    elif args.action in ["d", "debug"]:
        debug_brainfuck(args.file, CELL_MAX, WRAP_AROUND)
    else:
        print("Choose a valid action r/run or d/debug.")
        sys.exit(1)

def run_brainfuck(file_path, cell_max, wrap_around):
    if file_path:
        try:
            with open(file_path, "r") as f:
                code = f.read()
        except FileNotFoundError:
            print(f"Error: File with name '{file_path}' doesn't exist.")
            return
    else:
        code = input("Enter your code: ")

    interpreter = BrainfuckInterpreter(code, cell_max, wrap_around)
    interpreter.run()

def debug_brainfuck(file_path, cell_max, wrap_around):
    if file_path:
        try:
            with open(file_path, "r") as f:
                code = f.read()
        except FileNotFoundError:
            print(f"Error: File with name '{file_path}' doesn't exists.")
            return
    else:
        code = input("Enter your Brainfuck code for debug: ")

    debugger = BrainfuckDebugger(code, cell_max, wrap_around)
    debugger.run_debug()

if __name__ == "__main__":
    main()

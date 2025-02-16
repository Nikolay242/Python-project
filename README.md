This project is an interpreter and debugger for the Brainfuck programming language. It allows you to execute and debug Brainfuck programs via the command line. You can either input the code directly into the console or load it from a file.

INSTALATION
..........

USAGE
Running the Interpreter
To run the Brainfuck interpreter, use the following command:
python main.py r

If you want to use a file, provide the file path with the --file flag:
python main.py r --file <path_to_file> --cell-size 16

You can also change the cell size (default is 8):
python main.py r --cell-size 16

Running the Debugger
To debug a Brainfuck program, use the command:
python main.py d

If you want to debug a file, use:
python main.py d --file <path_to_file> --cell-size 16

Options:
--f, --file: Path to a Brainfuck program file.
--cell-size: Size of the cells (can be 8, 16, 32, or 64 bits).
--no-wrap: Disables wrap-around (prevents overflow and underflow).

Examples:
Run the program:
python main.py r

Debug a program:
python main.py d --file path/to/brainfuck-file.bf

Debug with a custom cell size:
python main.py d --file path/to/brainfuck-file.bf --cell-size 16
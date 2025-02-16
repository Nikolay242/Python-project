# Brainfuck Interpreter & Debugger

This project is an interpreter and debugger for the **Brainfuck** programming language. It allows you to execute and debug Brainfuck programs via the command line. You can either input the code directly into the console or load it from a file.

## Installation

To install and set up the project on your local machine, follow these steps:

### 1. Clone the repository
```sh
 git clone https://github.com/Nikolay242/Brainfuck-Interpreter.git
```

### 2. Navigate to the project directory
```sh
 cd Brainfuck-Interpreter
```

### 3. Install dependencies (if any)
This project doesn't require additional dependencies, but if you're using **Colorama** for colored output, install it with:
```sh
 pip install colorama
```

## Usage

### Running the Interpreter
To run the Brainfuck interpreter, use:
```sh
 python main.py r
```

If you want to run a Brainfuck file, provide the file path:
```sh
 python main.py r --file <path_to_file>
```

You can also change the cell size (default is 8-bit):
```sh
 python main.py r --cell-size 16
```

### Running the Debugger
To debug a Brainfuck program, use:
```sh
 python main.py d
```

If you want to debug a file, use:
```sh
 python main.py d --file <path_to_file>
```

You can also specify a custom cell size:
```sh
 python main.py d --file <path_to_file> --cell-size 16
```

### Options
- `-f, --file`: Path to a Brainfuck program file.
- `--cell-size`: Size of the cells (can be **8, 16, 32, or 64** bits).
- `--no-wrap`: Disables wrap-around (prevents overflow and underflow).

### Examples
Run a program:
```sh
 python main.py r
```

Run a program from a file:
```sh
 python main.py r --file path/to/brainfuck-file.bf
```

Debug a program:
```sh
 python main.py d --file path/to/brainfuck-file.bf
```

Debug with a custom cell size:
```sh
 python main.py d --file path/to/brainfuck-file.bf --cell-size 16
```

## License
This project is open-source and available under the [MIT License](LICENSE).

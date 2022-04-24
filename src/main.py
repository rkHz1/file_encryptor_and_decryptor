"""Python encryptor and decryptor

Usage:
    main.py (enc) <file_path> <key> <output_filename> [--showerrors]
    main.py (dec) <file_path> <key> <output_filename> [--showerrors]
    main.py --version

Options:
    --showerrors  prompts errors to console.
    --version     Show version.
    -h --help     Show this screen.
"""

from docopt import docopt
import functions


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Python encryptor and decryptor 1.1')

    if arguments["enc"]:
        try:
            k = functions.encrypyFile(arguments["<file_path>"], arguments["<output_filename>"], arguments["<key>"])
            print(k, end="")
        except functions.exeptions.fileDoesNotExist:
            if arguments["--showerrors"]:
                print("Error: file does not exist")
                exit(1)
            else:
                print(0, end="")
                exit(1)
        except functions.exeptions.isNotFile:
            if arguments["--showerrors"]:
                print("Error: indicated path is not a file")
                exit(1)
            else:
                print(0, end="")
                exit(1)
    elif arguments["dec"]:
        try:
            k = k = functions.decryptFile(arguments["<file_path>"], arguments["<output_filename>"], arguments["<key>"])
            print(k, end="")
        except functions.exeptions.fileDoesNotExist:
            if arguments["--showerrors"]:
                print("Error: file does not exist")
                exit(1)
            else:
                print(0, end="")
                exit(1)
        except functions.exeptions.isNotFile:
            if arguments["--showerrors"]:
                print("Error: indicated path is not a file")
                exit(1)
            else:
                print(0, end="")
                exit(1)
        except functions.exeptions.invalidKey:
            if arguments["--showerrors"]:
                print("Error: Invalid key")
                exit(1)
            else:
                print(0, end="")
                exit(1)
    
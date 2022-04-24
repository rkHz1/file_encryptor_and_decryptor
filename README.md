## Python file encrytptor and decryptor
![Python version badge](https://img.shields.io/badge/python-3.9-blue) ![App version badge](https://img.shields.io/badge/version-1.0.0-lightgrey) ![App version badge](https://img.shields.io/badge/dependencies-recent-green)
This program provides functions to aply symmetric encryption to any file 
from the command line.

### Arguments
`(enc|dec) <absolute_file_path> <key> <output_filename> [--showerrors]`
- (enc|dec) Mode: enc to encrypt mode, and dec to decrypt mode
- `<file_path>`: The absolute path to the file to encrypt or decrypt
- `<key>`: The encryption key
- `<output_filename>` Output filename
- `[--showerrors]` (optional): Use --showerrors to prompt errors to console

**Note**: all files are put in a "files" direcory in the working directory

----
### Prompts

The program prompts an error message if the command syntax is incorrect

In encrypt mode the program promps the encryption key in success
In decrypt mode the program prompts 1 (one) in success

If there is an error and the "--showerrors" is desactivated, the program prompts 0 (zero)
If there is an error and the "--showerrors" is activated, the program prompts an error mesage

---
### Dependencies
python 3.9
docopt
cryptography
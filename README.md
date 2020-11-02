# A1Z26 Decrypter
It's a simple script to decrypt A1Z26 Cipher.

## Install
```console
git clone https://github.com/KHPROG55/a1z26-decrypter
```

## Options
```console
$ python a1z26-decrypter
usage: a1z26-decrypter.py [-h]
                          [-s STRING [STRING ...]]
                          [-f FILE [FILE ...]] [-v]

optional arguments:
  -h, --help            show this help message and
                        exit
  -s STRING [STRING ...], --string STRING [STRING ...]
                        input a list of strings to
                        decipher them
  -f FILE [FILE ...], --file FILE [FILE ...]
                        input file(s) to decipher
                        it's content
  -v, --version         show program's version
                        number and exit
```

## Usage
```console
$ # decrypt a string
$ python a1z26-decrypter -s 20 5 19 20 9 14 7
testing
$ # decrypt a file
$ python a1z26-decrypter -f filename.txt
output here
$ # decrypt multiple files
$ python a1z26-decrypter -f file1.txt file2.txt ...
output file1.txt
output file2.txt
...
```

## License
`a1z26-decrypter` is licensed under the [**GNU General Public License (GPL) 3.0**](https://www.gnu.org/licenses/gpl.html). 

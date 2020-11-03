# A1Z26 Decrypter
It's a simple script to decrypt A1Z26 Cipher.

## Install
```console
git clone https://github.com/KHPROG55/a1z26-decrypter
```

## Options
```console
$ python a1z26-decrypter.py
usage: a1z26-decrypter.py [-h] [-e ENCRYPT [ENCRYPT ...]]
                          [-d DECRYPT [DECRYPT ...]] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -e ENCRYPT [ENCRYPT ...], --encrypt ENCRYPT [ENCRYPT ...]
                        Encrypt one or list of strings
                        from stdin or file(s)
  -d DECRYPT [DECRYPT ...], --decrypt DECRYPT [DECRYPT ...]
                        Decrypt one or list of strings
                        from stdin or file(s)
  -v, --version         show program's version number and
                        exit
```

## Usage
```console
$ # encrypt a string
$ python a1z26-decrypter.py -e testing
20 5 19 20 9 14 7
$ # decrypt a string
$ python a1z26-decrypter -d 20 5 19 20 9 14 7
testing
$ # encrypt from a file, inside the file > "testing"
$ python a1z26-decrypter -e filename.txt
20 5 19 20 9 14 7
$ # decrypt from a file  inside the file > "20 5 19 20 9 14 7"
$ python a1z26-decrypter -d filename.txt
testing
$ # encrypt from multiple files
$ python a1z26-decrypter -e file1.txt file2.txt ...
output of file1.txt
output of file2.txt
...
$ # decrypt from multiple files
python a1z26-decrypter -d file1.txt file2.txt ...
output of file1.txt
output of file2.txt
...
```

## License
`a1z26-decrypter` is licensed under the [**GNU General Public License (GPL) 3.0**](https://www.gnu.org/licenses/gpl.html). 

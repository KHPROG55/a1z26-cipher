import os, sys, argparse, fileinput

# Coded by KH PROG
# Source:
# https://github.com/KHPROG55/a1z26-decrypter

def a1z26_encrypt(inp):
    out = ""
    for i in inp:
        if i.isalpha():
            character = ord(i) - 96
            out += str(character) + " "
        else:
            out += str(i) + " "
    print(out, end ="")

def a1z26_decrypt(inp):
    out = ""
    for i in inp:
        if i.isdigit():
            character = int(i) + 96
            if 97 <= character <= 122:
                out += chr(character)
        else:
            i = str(i)
            out += i
    print(out, end="")

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encrypt", help="Encrypt one or list of strings from stdin or file(s)", nargs="+")
    parser.add_argument("-d", "--decrypt", help="Decrypt one or list of strings from stdin or file(s)", nargs="+")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 3.0")
    args = parser.parse_args()

    # -e option
    if args.encrypt:
        for i in args.encrypt:
            if os.path.isfile(i):
                with open(i, "r") as o:
                    a1z26_encrypt(o.read().strip().lower())
            if not os.path.isfile(i):
                a1z26_encrypt(i.strip().lower())

    # -d option
    if args.decrypt:
        for i in args.decrypt:
            if os.path.isfile(i):
                with open(i, "r") as o:
                    a1z26_decrypt(o.read().strip().lower().split(" "))
            if not os.path.isfile(i):
                a1z26_decrypt(i.strip().lower().split(" "))

    if not any(vars(args).values()):
        parser.print_help(sys.stderr)
        sys.exit()

if __name__ == "__main__":
   main(sys.argv)

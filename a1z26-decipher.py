import sys, argparse

# Coded by KH PROG
# Source:
# https://github.com/KHPROG55/a1z26-decipher

def a1z26_decipher(inp):
    out = ""
    for i in inp:
        if i.isdigit():
            character = int(i) + 96
            if 97 <= character <= 122:
                out += chr(character)
        else:
            i = str(i)
            out += i
    print(out)

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", help="input a list of strings to decipher them", nargs="+")
    parser.add_argument("-f", "--file", help="input file(s) to decipher it's content", type=argparse.FileType('r'), nargs="+")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 2.0")
    args = parser.parse_args()

    # -s option
    if args.string:
        inp = args.string
        a1z26_decipher(inp)

    # -f option
    if args.file:
        for f in args.file:
            a1z26_decipher(f.read().strip().split(" "))

    if not any(vars(args).values()):
        parser.print_help(sys.stderr)
        sys.exit()

if __name__ == "__main__":
   main(sys.argv)

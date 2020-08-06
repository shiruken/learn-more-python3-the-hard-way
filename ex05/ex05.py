import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('files', metavar='files', type=Path, nargs='+')
parser.add_argument('-n', '--numbered', help='Number the output lines, starting at 1.', action='store_true')
args = parser.parse_args()

linenumber = 1
for file in args.files:
    with open(file) as f:

        if args.numbered:
            for line in f.readlines():
                print(f"\t{linenumber}\t{line}", end="")
                linenumber += 1
        else:
            print(f.read())
            
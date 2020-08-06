import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--copy', help='Copy mode enabled', action='store_true')
parser.add_argument('-d', '--delete', help='Delete mode enabled', action='store_true')
parser.add_argument('-a', '--archive', help='Archive mode enabled', action='store_true')
parser.add_argument('-p', '--path', help='Set path')
parser.add_argument('-t', '--timeout', type=int, help='Set timeout in seconds')
parser.add_argument('-s', '--start', type=int, help='Set start in seconds')
parser.add_argument('files', metavar='files', type=Path, nargs='+')

args = parser.parse_args()
print(args)
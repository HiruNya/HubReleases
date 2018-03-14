import github_api
import simple_ver
import index
import argparse

COL2 = 10

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="cmd")
parser_ver = subparsers.add_parser(
    "get",
    help="Checks the current version listed in the index")
parser_ver.add_argument("name", help="The name of the release")
args = parser.parse_args()

if args.cmd == "get":
    x = index.get(args.name.lower())
    if x is not None:
        print(args.name, '=>')
        print('  Version'.ljust(COL2), x['version'])
        print('  Path'.ljust(COL2), x['path'])
    else:
        print(f'Error: File "{args.name}" could not be found in the index.')

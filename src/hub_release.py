import github_api
import simple_ver
import index
import argparse

COL2 = 10

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="cmd")
# hb get [name]
parser_ver = subparsers.add_parser(
    "get",
    help="Checks the current version listed in the index")
parser_ver.add_argument("name", help="The name of the program")
# hb check [name]
parser_check = subparsers.add_parser(
    "check",
    help="Compares the version listed in the index to the latest version on Github")
parser_check.add_argument("name", help="The name of the program")
# hb list
subparsers.add_parser(
    "list",
    help="Lists all the programs in the index"
)

args = parser.parse_args()

if args.cmd == "get":
    x = index.get(args.name.lower())
    if x is not None:
        print(args.name, '=>')
        print('  Version'.ljust(COL2), x['version'])
        print('  Path'.ljust(COL2), x['path'])
    else:
        print(f'Error: Program "{args.name}" could not be found in the index.')
elif args.cmd == "check":
    index_data = index.get(args.name.lower())
    if (index_data is not None):
        github_data = github_api.get_newest_release(index_data['path'])
        if (github_data is not None):
            x = simple_ver.compare(github_data.tag_name, index_data["version"])
            if x == 0:
                print("Github version is equal to your version")
            elif x == 1:
                print("New Update Available!")
                print("Current version -> Github version")
                print(index_data['version'].ljust(15), '->', github_data.tag_name)
    else:
        print(f'Error: Program "{args.name}" could not be found in the index.')
elif args.cmd == "list":
    index_data = index.get_all()
    for i in index_data.keys():
        print(i, "=>")
        print("  Version".ljust(COL2), index_data[i]['version'])
        print("  Path".ljust(COL2), index_data[i]['path'])

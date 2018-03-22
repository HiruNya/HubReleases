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
# hb add
parser_add = subparsers.add_parser(
    "add", help="Adds a program to the index"
)
parser_add.add_argument("-n", "--name", help="The name of the program")
parser_add.add_argument("-p", "--path", help="The url path of the github repo")
parser_add.add_argument("-v", "--version", help="The version of your program")

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
                print(f"URL: {github_data.url}")
                choice = input("Would you like to open this in the browser? (y/n): ").lower().strip(" ")
                if choice.startswith("y"):
                    from webbrowser import open as open_url
                    open_url(github_data.url, new=2)
                choice = input("Did you update the program? (y/n): ").lower().strip(" ")
                if choice.startswith("y"):
                    if index.update(args.name.lower(), github_data.tag_name):
                        print("Successfully updated!")
                    else:
                        print("Error in updating the entry in the index! ~ KeyError")
    else:
        print(f'Error: Program "{args.name}" could not be found in the index.')
elif args.cmd == "list":
    index_data = index.get_all()
    for i in index_data.keys():
        print(i, "=>")
        print("  Version".ljust(COL2), index_data[i]['version'])
        print("  Path".ljust(COL2), index_data[i]['path'])
elif args.cmd == "add":
    if args.name is None:
        name = input("Name: ").lower().strip(" ")
    else: name = args.name
    if args.path is None:
        path = input("Repo's Path/URL: ")
    else: path = args.path
    path = path.lstrip("http").lstrip("s").lstrip("://").lstrip("www.").lstrip("github.com/").rstrip("/releases")
    print(f'Recorded Path as: {path}')
    if args.version is None:
        choice = input("Would you like us to use the current version from GitHub? (y/n): ").lower().strip(" ")
        if choice.startswith("y"):
            repo = github_api.get_newest_release(path)
            if repo is None:
                print(f"No repo with the path {path} was found")
                raise KeyError
            else:
                version = repo.tag_name
                print(f"Current version is {version}")
        else: version = input("Version: ")
    else: version = args.version
    if index.check_and_insert(name, version, path):
        print(f"Program {name} added to the index!")
    else:
        print('Error! That name is already present in the index. Use the "change" command instead.')

else:
    print("Use the -h command to get a list of the commands usable.")

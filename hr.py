from src import github_api, simple_ver, index
import argparse

COL2 = 10

def parse_path(path):
    return path.replace("http://", "").replace("https://", "").replace("www.", "").replace("github.com/", "").replace("/releases", "")

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
parser_add.add_argument("-e", "--exact", action="store_true", help="Use the exact path without parsing it (Only use it's not working as intended)")

# hb del
parser_del = subparsers.add_parser(
    "del", help="Removes a program from the index"
)
parser_del.add_argument("name", help="The name of the program")
#hb update
parser_update = subparsers.add_parser(
    "update", help="Updates a program int he index manually"
)
parser_update.add_argument("name", help="The name of the program currently")
parser_update.add_argument("-n", "--new_name", help="The name you want to rename the program to")
parser_update.add_argument("-p", "--path", help="The new path")
parser_update.add_argument("-v", "--version", help="The version you wish to update it to")
parser_update.add_argument("-e", "--exact", action="store_true", help="Use the exact path without parsing it (Only use it's not working as intended)")

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
    path = args.path if args.exact else parse_path(args.path)
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
elif args.cmd == "del":
    name = args.name.lower()
    if index.delete(name):
        print(f"Program {name} was removed from the index.")
    else: print("No such program exists.")
elif args.cmd == "update":
    if index.check(args.name):
        n_data = {}
        if args.path is not None:
            n_data["path"] = args.path if args.exact else parse_path(args.path)
        if args.version is not None:
            n_data["version"] = args.version
        if args.new_name is not None:
            if index.check(args.new_name):
                print("That name is already taken.")
                raise KeyError
        index.update_manual(args.name, n_data, args.new_name)
    else:
        print("That program was not found in the index.")

else:
    print("Use the -h command to get a list of the commands usable.")

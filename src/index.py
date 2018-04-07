from yaml import load, dump
FILE = "index.yaml"

def get_all():
    with open(FILE, "r") as file:
        return load(file.read())

def get(key):
    with open(FILE) as file:
        try:
            data = load(file.read())[key]
        except KeyError:
            return None
    return data

def check(key):
    with open(FILE) as file:
        if key in load(file.read()):
            return True
        else:
            return False

def check_and_insert(key, version, path):
    with open(FILE, "r") as file:
        data = load(file.read())
    if key in data:
        return False
    else:
        data[key] = {
            "version": version,
            "path": path,
        }
        with open(FILE, "w") as file:
            file.write(dump(data))
        return True

def update(key, version):
    with open(FILE, "r") as file:
        data = load(file.read())
    try:
        data[key]["version"] = version
    except KeyError:
        return False
    with open(FILE, "w") as file:
        file.write(dump(data))
    return True

def update_manual(key, n_data, new_name=None):
    with open(FILE, "r") as file:
        c_data = load(file.read())
    try:
        for i in n_data.keys():
            c_data[key][i] = n_data[i]
        if new_name is not None:
            c_data[new_name]
        with open(FILE, "w") as file:
            file.write(dump(c_data))
    except KeyError:
        print("A key error ocurred when manually updating the index file.\nNothing was saved.")

def delete(key):
    with open(FILE, "r") as file:
        data = load(file.read())
    try:
        del data[key]
        with open(FILE, "w") as file:
            file.write(dump(data))
        return True
    except KeyError:
        return False

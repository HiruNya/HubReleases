from yaml import load
FILE = "../index.yaml"

def get_all():
    with open(FILE) as file:
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

def check_and_insert(key, version, path, cont=False):
    with open(FILE, "w") as file:
        data = load(file.read())
        if key in data:
            return False
        else:
            data[key] = {
                "version": version,
                "path": path,
            }
            return True
        file.write(data)

def update(key, version):
    with open(FILE, "w") as file:
        data = load(file.read())
    try:
        data[key] = version
        return True
    except KeyError:
        return False

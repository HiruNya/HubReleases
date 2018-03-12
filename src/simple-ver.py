def version(inp: str):
    stripped_string = ''.join(list(filter(lambda x: x in "0123456789.", inp)))
    versions = stripped_string.split('.')
    length = len(versions)
    if 0 < length:
        for i in range(len(versions)):
            versions[i] = int(versions[i])
        return versions
    else:
        return False
def compare(x: str, y: str):
    # Will return:
    # 0 ~ Equal versions
    # 1 ~ First variable is higher
    # 2 ~ Second variable is higher
    x, y = version(x), version(y)
    if len(x) <= len(y):
        for i in range(len(x)):
            if x[i] != y[i]:
                if x[i] > y[i]:
                    return 1
                else:
                    return 2
        return 0
    else:
        for i in range(len(y)):
            if x[i] != y[i]:
                if x[i] > y[i]:
                    return 1
                else:
                    return 2
        return 0
if __name__ == "__main__":
    c = compare('3.7.1', '3.6.1')
    print(c)

def i(source):
    return "i%se" % str(source)


def s(source):
    return "%d:%s" % (len(source), source)


def l(source):
    result = []

    for item in source:
        result.append(encode(item))

    return "l%se" % ''.join(result)


def d(source):
    result = []
    source = [item for sublist in source.items() for item in sublist]

    for item in source:
        result.append(encode(item))

    return "d%se" % ''.join(result)


def encode(source):
    types = {
        int: i,
        str: s,
        list: l,
        dict: d
    }

    return types[type(source)](source)

if __name__ == '__main__':
    # i123e
    print(encode(123))

    # 12:Hello World!
    print(encode("Hello World!"))

    # l4:spam4:eggse
    print(encode(["spam", "eggs"]))

    # l3:abc3:abcl3:abcel3:abcee
    print(encode(['abc', 'abc', ['abc'], ['abc']]))

    # d3:cow3:moo4:spam4:eggse
    print(encode({'cow': 'moo', 'spam': 'eggs'}))

    # d3:cow3:moo4:spaml5:eggsA5:eggsBi123eee
    print(encode({'cow': 'moo', 'spam': ['eggsA', 'eggsB', 123]}))


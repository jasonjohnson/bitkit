def i(source):
    return "i%se" % str(source)

def s(source):
    return "%d:%s" % (len(source), source)

def l(source):
    result = []
    types = {
        int:  i,
        str:  s,
        list: l,
        dict: d
    }

    for item in source:
        result.append(types[type(item)](item))

    return "l%se" % ''.join(result)

def d(source):
    pass

if __name__ == '__main__':
    # i123e
    print(i(123))

    # 12:Hello World!
    print(s("Hello World!"))

    # l4:spam4:eggse
    print(l(["spam", "eggs"]))

    # l3:abc3:abcl3:abcel3:abcee
    print(l(['abc', 'abc', ['abc'], ['abc']]))

    # d3:cow3:moo4:spam4:eggse
    print(d({'cow': 'moo', 'spam': 'eggs'}))

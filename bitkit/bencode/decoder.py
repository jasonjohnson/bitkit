from string import digits


class Decoder(object):
    def __init__(self, source):
        self.offset = 0
        self.source = source

    def current(self):
        return self.source[self.offset]

    def step(self):
        self.offset += 1

    def i(self):
        result = []
        
        self.step()
        
        while self.current() in digits:
            result.append(self.current())
            self.step()

        self.step()

        return int(''.join(result))
    
    def s(self):
        result = []
        length = []
        
        while self.current() in digits:
            length.append(self.current())
            self.step()
        
        length = int(''.join(length))

        self.step()

        for i in range(length):
            result.append(self.current())
            self.step()

        return ''.join(result)

    def l(self):
        pieces = []

        self.step()

        while self.current() != 'e':
            pieces.append(self.decode())
        
        self.step()

        return pieces

    def d(self):
        pieces = self.l()
        return dict(zip(pieces[0::2], pieces[1::2]))

    def decode(self):
        if self.current() in digits:
            return self.s()
        elif self.current() == 'd':
            return self.d()
        elif self.current() == 'l':
            return self.l()
        elif self.current() == 'i':
            return self.i()


def decode(source):
    return Decoder(source).decode()

if __name__ == '__main__':
    # {'cow': 'moo', 'spam': 'eggs'}
    print(decode("d3:cow3:moo4:spam4:eggse"))

    # ['spam', 'eggs']
    print(decode("l4:spam4:eggse"))

    # ['abc', 'abc', ['abc'], ['abc']]
    print(decode("l3:abc3:abcl3:abcel3:abcee"))

    # 123
    print(decode("i123e"))

    # spam
    print(decode("4:spam"))

    # Now, pull in some .torrent files and see if we can
    # decode them. Including all the pieces data.
    from os import listdir
    from os.path import dirname, realpath, join

    torrents = join(dirname(dirname(realpath(__file__))), 'torrents')

    for torrent in listdir(torrents):
        with open(join(torrents, torrent)) as t:
            decoded = decode(t.read())

            print(decoded)
            print(decoded.keys())


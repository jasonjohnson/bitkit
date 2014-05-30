import hashlib
import os
import os.path

from bitkit.bencode import encode


def get_name(source):
    return os.path.basename(source)


def get_length(source):
    with open(source, 'rb') as src:
        src.seek(0, os.SEEK_END)
        return src.tell()


def get_pieces(source, step):
    pieces = []

    with open(source, 'rb') as src:
        while True:
            chunk = src.read(step)

            if not chunk:
                break

            func = hashlib.new('sha1')
            func.update(chunk)

            pieces.append(func.digest())

    return ''.join(pieces)


def create(source, torrent, step, announce):
    with open(torrent, 'wb') as torrent:
        torrent.write(encode({
            "announce": announce,
            "info": {
                "name": get_name(source),
                "length": get_length(source),
                "pieces": get_pieces(source, step),
                "piece length": step
            }
        }))


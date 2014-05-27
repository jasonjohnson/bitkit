# bitkit

A collection of tools for BitTorrent users and tracker administrators.

## Tools

**bitkit** bundles 3 tools. A basic single-torrent client, a torrent creator, and a torrent tracker. Each tool is exposed via a sub-command of the ```bitkit``` command.

```
$ bitkit
usage: bitkit [-h] {client,create,tracker} ...
```

### Single-Torrent Client

```
$ bitkit client -h
usage: bitkit client [-h] torrent

positional arguments:
  torrent

optional arguments:
  -h, --help  show this help message and exit
```

### Torrent Creator

```
$ bitkit create -h
usage: bitkit create [-h] [--step STEP] [--announce ANNOUNCE] source torrent

positional arguments:
  source
  torrent

optional arguments:
  -h, --help           show this help message and exit
  --step STEP
  --announce ANNOUNCE
```

### Tracker

```
$ bitkit tracker -h
usage: bitkit tracker [-h] [--port PORT] [--address ADDRESS]

optional arguments:
  -h, --help         show this help message and exit
  --port PORT
  --address ADDRESS
```

## Codec

Additionally, the **bencode** codec in *bitkit* is available as a library. Simply add *bitkit* to your project as a dependency and use the 2-function interface.

```python
from bitkit.bencode import decode, encode

original = {
    "a": 1,
    "b": "two",
    "c": ["one", "two", 3],
    "d": {"e": [4, 5, 6]}
}

# Encode our complex data structure into
# the bencode format.
encoded = encode(original)

# d1:ai1e1:cl3:one3:twoi3ee1:b3:two1:dd1:eli4ei5ei6eeee
print(encoded)

# Now, reverse the process.
decoded = decode(encoded)

# {'a': 1, 'c': ['one', 'two', 3], 'b': 'two', 'd': {'e': [4, 5, 6]}}
print(decoded)
```

## References

* http://bittorrent.org/beps/bep_0000.html
* http://bittorrent.org/beps/bep_0003.html
* https://wiki.theory.org/BitTorrentSpecification
* http://www.kristenwidman.com/blog/how-to-write-a-bittorrent-client-part-1/
* http://www.kristenwidman.com/blog/how-to-write-a-bittorrent-client-part-2/


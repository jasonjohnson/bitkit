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
usage: bitkit create [-h] source torrent

positional arguments:
  source
  torrent

optional arguments:
  -h, --help  show this help message and exit
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

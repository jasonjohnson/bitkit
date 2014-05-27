import argparse
import sys


def client(args):
    print(args.torrent)


def create(args):
    print(args.source)
    print(args.torrent)


def tracker(args):
    print(args.port)
    print(args.address)


def command(cmd):
    return {"client": client,
            "create": create,
            "tracker": tracker}.get(cmd)


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command")

    client_parser = commands.add_parser("client")
    client_parser.add_argument("torrent")

    create_parser = commands.add_parser("create")
    create_parser.add_argument("source")
    create_parser.add_argument("torrent")

    tracker_parser = commands.add_parser("tracker")
    tracker_parser.add_argument("--port", type=int, default=9090)
    tracker_parser.add_argument("--address", type=str, default="0.0.0.0")

    args = parser.parse_args(sys.argv[1:])

    command(args.command)(args)

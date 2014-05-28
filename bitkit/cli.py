import argparse
import sys

import bitkit.tools


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command")

    client = commands.add_parser("client")
    client.add_argument("torrent")

    create = commands.add_parser("create")
    create.add_argument("--step", type=int, default=512*1024)
    create.add_argument("--announce", type=str, default="http://127.0.0.1:9090/announce")
    create.add_argument("source")
    create.add_argument("torrent")

    tracker = commands.add_parser("tracker")
    tracker.add_argument("--port", type=int, default=9090)
    tracker.add_argument("--address", type=str, default="0.0.0.0")

    # Discard the Namespace object. It's easier just to
    # work with a dictionary.
    args = vars(parser.parse_args(sys.argv[1:]))

    # We won't need the command inside the implementation.
    # Just use it to dispatch into the tool.
    getattr(bitkit.tools, args.pop('command'))(**args)

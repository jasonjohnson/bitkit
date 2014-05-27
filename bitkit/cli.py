import argparse
import sys

import bitkit.tools


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command")

    client_parser = commands.add_parser("client")
    client_parser.add_argument("torrent")

    create_parser = commands.add_parser("create")
    create_parser.add_argument("--step", type=int, default=512*1024)
    create_parser.add_argument("--announce", type=str, default="http://127.0.0.1:9090/announce")
    create_parser.add_argument("source")
    create_parser.add_argument("torrent")

    tracker_parser = commands.add_parser("tracker")
    tracker_parser.add_argument("--port", type=int, default=9090)
    tracker_parser.add_argument("--address", type=str, default="0.0.0.0")

    args = parser.parse_args(sys.argv[1:])

    getattr(bitkit.tools, args.command)(args)

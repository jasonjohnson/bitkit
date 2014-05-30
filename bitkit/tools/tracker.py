from urlparse import parse_qs
from wsgiref.simple_server import make_server

from bitkit.bencode import encode


torrents = {}


def app(env, start_response):
    path = env.get("PATH_INFO")
    query = parse_qs(env.get("QUERY_STRING"))

    # Extract what we need from env and query string. We'll
    # use this to populate/clobber existing peer data about
    # this torrent.
    ip = env["REMOTE_ADDR"]
    port = query.get("port")[0]
    peer = query.get("peer_id")[0]
    torrent = query.get("info_hash")[0]

    if torrent not in torrents:
        torrents[torrent] = {}

    torrents[torrent][peer] = {"ip": ip, "port": int(port)}

    peers = []

    for peer, address in torrents[torrent].items():
        peers.append({"peer id": peer,
                      "ip": address.get("ip"),
                      "port": address.get("port")})

    start_response("200 OK", [("Content-Type", "text/plain")])

    return encode({"interval": 1,
                   "complete": 0,
                   "incomplete": 0,
                   "peers": peers})


def tracker(address, port):
    print("Tracker started: http://%s:%d" % (address, port))
    print("--")

    server = make_server(address, port, app)
    server.serve_forever()


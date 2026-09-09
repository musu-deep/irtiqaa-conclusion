import os
import sys
import socket
import threading
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

import webview


def resource_path(*parts):
    base = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(base, *parts)


def find_free_port(preferred=8027):
    candidates = [preferred] + list(range(preferred + 1, preferred + 20))
    for port in candidates:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("No free port found")


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def start_server(port, directory):
    handler = partial(QuietHandler, directory=directory)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), handler)
    httpd.serve_forever()


def main():
    base_dir = resource_path()
    port = find_free_port(8027)
    server_thread = threading.Thread(
        target=start_server,
        args=(port, base_dir),
        daemon=True
    )
    server_thread.start()

    url = f"http://127.0.0.1:{port}/index.html"
    webview.create_window(
        title="ERTIQA Observatory",
        url=url,
        width=1440,
        height=920,
        min_size=(1200, 760),
        text_select=True
    )
    webview.start()


if __name__ == "__main__":
    main()

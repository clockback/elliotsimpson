import http.server
import socketserver
from pathlib import Path

PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    directory = Path(__file__).parent / "src"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)


def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()

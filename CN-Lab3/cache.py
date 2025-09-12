import http.server
import socketserver
import os
import hashlib
from datetime import datetime
from email.utils import formatdate

PORT = 8000
FILE_TO_SERVE = "index.html"


def generate_etag(file_path):
    """Generate an MD5-based ETag for the file."""
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return f'"{file_hash}"'


def get_last_modified(file_path):
    """Return the file's last modified time in HTTP-date format."""
    mtime = os.path.getmtime(file_path)
    return formatdate(timeval=mtime, usegmt=True)


class CachingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Always serve the same file regardless of path
        if self.path == '/':
            self.path = FILE_TO_SERVE

        file_path = self.translate_path(self.path)

        if not os.path.exists(file_path):
            self.send_error(404, "File not found")
            return

        etag = generate_etag(file_path)
        last_modified = get_last_modified(file_path)

        # Extract request headers from client
        client_etag = self.headers.get("If-None-Match")
        client_last_modified = self.headers.get("If-Modified-Since")

        # Check ETag match (strong validator)
        if client_etag == etag:
            self.send_response(304)
            self.end_headers()
            return

        # Check Last-Modified (weak validator)
        if client_last_modified == last_modified:
            self.send_response(304)
            self.end_headers()
            return

        # Otherwise send the file with caching headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("ETag", etag)
        self.send_header("Last-Modified", last_modified)
        self.end_headers()

        with open(file_path, "rb") as f:
            self.wfile.write(f.read())


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), CachingHTTPRequestHandler) as httpd:
        print(f"Serving on http://localhost:{PORT}")
        httpd.serve_forever()

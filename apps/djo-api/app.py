import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = "0.1.0"


class ApiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/version":
            status = 200
            payload = {"service": "djo-api", "version": VERSION}
        else:
            status = 404
            payload = {"error": "route inconnue"}

        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    host = os.getenv("DJO_BIND", "127.0.0.1")
    with HTTPServer((host, 18081), ApiHandler) as server:
        print(f"DJO API écoute sur {host}:18081", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import json
import os

APP_DIR = Path(__file__).parent

PORT = int(os.environ.get("PORT", "8000"))
class DevOpsHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            data = {"status": "healthy", "application": "Cloud DevOps Platform"}
            body = json.dumps(data).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        else:
            super().do_GET()

server = ThreadingHTTPServer(
    ("0.0.0.0", PORT),
    partial(DevOpsHandler, directory=str(APP_DIR))
)

print(f"Cloud DevOps Platform running on port {PORT}")
server.serve_forever()

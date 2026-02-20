import logging
import os
import re

from flask import Flask, jsonify, request

app = Flask(__name__)

# Basic structured logging
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
log = logging.getLogger("secure-api")

# Simple input validation
SAFE_NAME = re.compile(r"^[a-zA-Z0-9_-]{1,40}$")


@app.after_request
def set_security_headers(resp):
    # Security headers (minimal example; customize for your needs)
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Referrer-Policy"] = "no-referrer"
    resp.headers["Content-Security-Policy"] = (
        "default-src 'none'; frame-ancestors 'none'; base-uri 'none'"
    )
    resp.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    return resp


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/hello")
def hello():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name", "")
    if not isinstance(name, str) or not SAFE_NAME.match(name):
        log.warning("Invalid input", extra={"input_name": str(name)[:80]})
        return jsonify(error="Invalid name. Use 1-40 chars: letters, digits, _ or -"), 400
    return jsonify(message=f"Hello, {name}!")


@app.errorhandler(Exception)
def handle_exception(e):
    # Avoid leaking internals; log server-side
    log.exception("Unhandled exception")
    return jsonify(error="Internal server error"), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))

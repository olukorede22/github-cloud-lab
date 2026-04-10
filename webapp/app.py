from flask import Flask, jsonify
import socket
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route("/")
def index():
    try:
        count = cache.incr("hits")
    except redis.exceptions.ConnectionError:
        count = "unavailable"
    return f"GitHub Cloud Lab\n\nThis page has been visited {count} times."

@app.route("/info")
def info():
    hostname = socket.gethostname()
    return jsonify({
        "hostname": hostname,
        "version": "v1",
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

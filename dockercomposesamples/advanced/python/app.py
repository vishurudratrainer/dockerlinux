import os
from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis using environment variables set in docker-compose.yml
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
cache = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello():
    # Increment visit count in Redis cache
    count = cache.incr('hits')
    return f'Hello from Python Flask! This page has been viewed {count} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
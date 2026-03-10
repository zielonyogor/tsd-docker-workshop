from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='db', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.\n' % redis.get('hits').decode('utf-8')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
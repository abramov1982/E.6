import os
from flask import Flask, request
from flask_caching import Cache
import random

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis',
                           'CACHE_REDIS_HOST': 'redis',
                           'CACHE_REDIS_PORT': 6379
                           })
port = int(os.environ.get('PORT', 5000))

@app.route('/')
@cache.cached(timeout=10)
def hello_world():
    data = str(random.randint(0,100000))  + '\n'
    return data

@app.route('/fib/<int:f_id>')
@cache.cached(timeout=600)
def fibonachchi(f_id):
    counter = f_id - 2
    fib_list = [0, 1]
    while counter > 0:
        fib_list[0], fib_list[1] = fib_list[1], fib_list[0] + fib_list[1]
        counter -= 1
    print(fib_list[1])
    return (f'{f_id} fibonachi = {fib_list[1]}')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

from flask import Flask

app = Flask(__name__)


@app.route('/test')
def hello():
    return "Test"


if __name__ == '__main__':  # if it's an entry point. then run Flask :O -> if it's not a module call then run Flask :D
    app.run(host='127.0.0.1', port=5000)


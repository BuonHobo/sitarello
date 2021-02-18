from flask import Flask  # pip install flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'<h1>Hello!</h1>'


@app.route('/about')
def about():
    return f'<h1>Hello!</h1>\nHai trovato la roba segreta'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

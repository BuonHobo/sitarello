from flask import Flask  # pip install flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return open("static/html/HTML.html").read()


@app.route('/about')
def about():
    return 'Sto facendo cose a caso'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

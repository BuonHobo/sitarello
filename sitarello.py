from flask import Flask,render_template  # pip install flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/about')
def about():
    return 'Sto facendo cose a caso'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

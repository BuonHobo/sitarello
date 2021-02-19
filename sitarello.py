from flask import Flask, render_template  # pip install flask
import crawler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html", articoli=articoli)


if __name__ == "__main__":
    articoli = crawler.get_articoli()
    app.run(debug=True)

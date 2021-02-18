from flask import Flask, render_template  # pip install flask
import crawler
app = Flask(__name__)
articoli = crawler.get_articoli()


@app.route('/')
def hello_world():
    return render_template("home.html", articoli=articoli)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

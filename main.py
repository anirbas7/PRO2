from flask import Flask
from flask import render_template



app = Flask("yatzy")

@app.route("/")
def start():
    return render_template("start.html")

@app.route('/yatzy')
def yazzi():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

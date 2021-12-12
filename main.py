from flask import Flask, request
from flask import render_template



app = Flask("yatzy")

@app.route("/", methods=['GET', 'POST'])
def start():
    if request.method == "POST":
        Spieler1 = request.form.get("Spieler1")
        return(Spieler1)
    else:
        return render_template("start.html")


@app.route('/yatzy')
def yazzi():
    return render_template("index.html")

@app.route('/nav')
def nav():
    return render_template("navbar.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

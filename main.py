from flask import Flask, request
from flask import render_template



app = Flask("yatzy")

@app.route("/", methods=['GET', 'POST'])
def start():
    if request.method == "POST":
        Spieler1 = request.form.get("Spieler1")
        Spieler2 = request.form.get("Spieler2")
        Spieler3 = request.form.get("Spieler3")
        Spieler4 = request.form.get("Spieler4")
        Spieler5 = request.form.get("Spieler5")
        Spieler6 = request.form.get("Spieler6")
        Spieler7 = request.form.get("Spieler7")
        Spieler8 = request.form.get("Spieler8")
        return(Spieler1 & Spieler2, Spieler3, Spieler4, Spieler5, Spieler6, Spieler7, Spieler8)

    else:
        return render_template("start.html")


@app.route('/yatzy')
def yatzy():
    return render_template("index.html")

@app.route('/nav')
def nav():
    return render_template("navbar.html")

@app.route('/test')
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

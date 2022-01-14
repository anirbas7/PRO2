from flask import Flask, request
from flask import render_template
import csv
app = Flask("yatzy")

@app.route("/", methods=['GET', 'POST'])
def start():
    if request.method == "POST":
        players =[]
        Spieler1 = request.form.get("Spieler1")
        players.append(Spieler1)
        Spieler2 = request.form.get("Spieler2")
        players.append(Spieler2)
        Spieler3 = request.form.get("Spieler3")
        players.append(Spieler3)
        Spieler4 = request.form.get("Spieler4")
        players.append(Spieler4)
        Spieler5 = request.form.get("Spieler5")
        players.append(Spieler5)
        Spieler6 = request.form.get("Spieler6")
        players.append(Spieler6)
        Spieler7 = request.form.get("Spieler7")
        players.append(Spieler7)
        Spieler8 = request.form.get("Spieler8")
        players.append(Spieler8)
        with open("Name.csv", "w+") as file:
            writer = csv.writer(file, delimiter=";")
            for player in towriter:
                players.append(player)
        return render_template("test2.html", spieler=player)

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

@app.route('/test2')
def test2():
    rows = []
    with open("8-Spieler.csv") as file:
        csvreader = csv.reader(file, delimiter=";")
        header = next(csvreader)
        for row in csvreader:
             rows.append(row)
    return render_template("test2.html", ergebnise=rows, tittel=header)

@app.route('/test3')
def test3():
    return render_template("test3.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

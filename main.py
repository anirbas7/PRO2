from flask import Flask, request
from flask import render_template
import csv
app = Flask("yatzy")\

@app.route("/", methods=['GET', 'POST'])
def start():
    if request.method == "POST":
        players = []
        spieler1 = request.form.get("Spieler1")
        players.append(spieler1)
        spieler2 = request.form.get("Spieler2")
        players.append(spieler2)
        spieler3 = request.form.get("Spieler3")
        players.append(spieler3)
        spieler4 = request.form.get("Spieler4")
        players.append(spieler4)
        spieler5 = request.form.get("Spieler5")
        players.append(spieler5)
        spieler6 = request.form.get("Spieler6")
        players.append(spieler6)
        spieler7 = request.form.get("Spieler7")
        players.append(spieler7)
        spieler8 = request.form.get("Spieler8")
        players.append(spieler8)
        with open("Name.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            for spieler in players:
                writer.writerow(spieler)
        return render_template("test2.html", spieler=players)
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
    rows = []
    with open("8-Spieler.csv") as file:
        csvreader = csv.reader(file, delimiter=";")
        header = next(csvreader)
        for row in csvreader:
             rows.append(row)
    return render_template("test.html", ergebnise=rows, tittel=header)

@app.route('/test2')
def test2():
    players = []
    rows = []
    with open("2-Spieler.csv") as file:
        csvreader = csv.reader(file, delimiter=";")
        header = next(csvreader)
        for row in csvreader:
             rows.append(row)
    with open("name2.csv") as file1:
        csvnamereader = csv.reader(file1, delimiter=";")
        for player in csvnamereader:
            players.append(player)
    return render_template("test2.html", ergebnise=rows, tittel=header, spieler=players)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, request
from flask import render_template
from flask import redirect
import csv
import shutil
import time
import sys
import pathlib
import os


def get_datadir() -> pathlib.Path:
    home = pathlib.Path.home()
    if sys.platform == "win32":
        return home / "AppData/Roaming"
    elif sys.platform == "linux":
        return home / ".local/share"
    elif sys.platform == "darwin":
        return home / "Library/Application Support"


my_datadir = get_datadir() / "yatzy"
try:
    my_datadir.mkdir(parents=False)
except FileExistsError:
    pass
try:
    f = open(os.path.join(my_datadir, 'Name.csv'), "x")
except FileExistsError:
    pass

app = Flask("yatzy")\



@app.route("/", methods=['GET', 'POST'])
def start():
    if request.method == "POST":
        players = ["Spielername"]
        spieler1 = request.form.get("Spieler1")
        if spieler1 != "":
            players.append(spieler1)
        spieler2 = request.form.get("Spieler2")
        if spieler2 != "":
            players.append(spieler2)
        spieler3 = request.form.get("Spieler3")
        if spieler3 != "":
            players.append(spieler3)
        spieler4 = request.form.get("Spieler4")
        if spieler4 != "":
            players.append(spieler4)
        spieler5 = request.form.get("Spieler5")
        if spieler5 != "":
            players.append(spieler5)
        spieler6 = request.form.get("Spieler6")
        if spieler6 != "":
            players.append(spieler6)
        spieler7 = request.form.get("Spieler7")
        if spieler7 != "":
            players.append(spieler7)
        spieler8 = request.form.get("Spieler8")
        if spieler8 != "":
            players.append(spieler8)
        original_stdout = sys.stdout
        namecsv = os.path.join(my_datadir, "Name.csv")
        with open(namecsv, 'w') as f0:
            sys.stdout = f0
            print(*players, sep=';')
            sys.stdout = original_stdout
        return redirect("/yatzy", code=301)
    else:
        return render_template("start.html")


@app.route('/yatzy', methods=['GET', 'POST'])
def yatzy():
    players = []
    namecsv = os.path.join(my_datadir, "Name.csv")
    with open(namecsv, "r") as f1:
        reader = csv.reader(f1)
        for row in reader:
            row = str(row).replace('\\', '')
            players = row.split(";", 9)
    player_count = str(len(players) - 1)
    zeit = time.strftime('%Y-%m-%d-%Hh%M', time.localtime())
    filename = (zeit + "-Sp-" + player_count + ".csv")
    destinationfile = os.path.join(my_datadir, filename)
    sourcefile = ("templates/spielplan/" + player_count + "-Spieler.csv")
    shutil.copy(namecsv, destinationfile, follow_symlinks=True)
    players = []
    rows = []
    with open(namecsv)as f2:
        csvreader = csv.reader(f2, delimiter=";")
        for player in csvreader:
            players.append(player)
    with open(destinationfile, "a+", encoding='utf-8-sig') as f3:
        with open(sourcefile, "r", encoding='utf-8-sig') as f4:
            f3.write(f4.read())
    with open(destinationfile) as f5:
        csvreader = csv.reader(f5, delimiter=";")
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    if request.method == "POST":
        points1 = []
        punktesp1 = request.form.get("pSp1[]")
        if punktesp1 != "":
            points1.append(punktesp1)
            print(points1)
        with open(destinationfile, 'r') as f6:
            points = list(f6)
            points[1:1].append(points1)
        print(points)
        original_stdout = sys.stdout
        with open(destinationfile, 'w') as f6:
            sys.stdout = f6
            print(*points1)
            sys.stdout = original_stdout
        return redirect("/yatzy", code=301)
    else:
        return render_template("index.html", ergebnise=rows, titel=header, spieler=players)


@app.route('/nav')
def nav():
    return render_template("navbar.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

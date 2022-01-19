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
        with open(namecsv, 'w') as f:
            sys.stdout = f
            print(*players, sep=';')
            sys.stdout = original_stdout
        return redirect("/yatzy", code=301)
    else:
        return render_template("start.html")


@app.route('/yatzy')
def yatzy():
    players = []
    print(my_datadir)
    namecsv = os.path.join(my_datadir, "Name.csv")
    print(namecsv)
    with open(namecsv, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            row = str(row).replace('\\', '')
            players = row.split(";", 9)
    player_count = str(len(players) -1)
    zeit = time.strftime('%Y-%m-%d-%Hh%M', time.localtime())
    filename = (zeit + "-Sp-" + player_count + ".csv")
    destinationfile = os.path.join(my_datadir, filename)
    sourcefile = ("templates/spielplan/" + player_count + "-Spieler.csv")
    shutil.copy(namecsv, destinationfile, follow_symlinks=True)
    with open(destinationfile,"a+") as f:
        with open(sourcefile,"r") as f1:
            f.write(f1.read())
    players = []
    with open(destinationfile) as f:
        csvnamereader = csv.reader(f, delimiter=";")
        for player in csvnamereader:
            players.append(player)
    return render_template("index.html", ergebnise=rows, tittel=header, spieler=players)

@app.route('/nav')
def nav():
    return render_template("navbar.html")

@app.route('/test')
def test():
    players = []
    rows = []
    """with open("8-Spieler.csv") as file:
        csvreader = csv.reader(file, delimiter=";")
        header = next(csvreader)
        for row in csvreader:
             rows.append(row)
    with open("name2.csv") as file1:
        csvnamereader = csv.reader(file1, delimiter=";")
        for player in csvnamereader:
            players.append(player)
    return render_template("test.html", ergebnise=rows, tittel=header, spieler=players)"""

@app.route('/test2')
def test2():
    players = []
    print(my_datadir)
    namecsv = os.path.join(my_datadir, "Name.csv")
    print(namecsv)
    with open(namecsv, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            row = str(row).replace('\\', '') #deleting backslash
            players = row.split(";", 9)
    player_count = str(len(players) -1)
    zeit = time.strftime('%Y-%m-%d-%Hh%M', time.localtime())
    filename = (zeit + "-Sp-" + player_count + ".csv")
    destinationfile = os.path.join(my_datadir, filename)
    sourcefile = ("templates/spielplan/" + player_count + "-Spieler.csv")
    shutil.copy(namecsv, destinationfile, follow_symlinks=True)
    with open(destinationfile,"a+") as f:
        with open(sourcefile,"r") as f1:
            f.write(f1.read())

    players = []
    rows = []
    with open("2-Spieler.csv") as file:
        csvreader = csv.reader(file, delimiter=";")
        header = next(csvreader)
        for row in csvreader:
             rows.append(row)
    with open("Name.csv") as file1:
        csvnamereader = csv.reader(file1, delimiter=";")
        for player in csvnamereader:
            players.append(player)
    return render_template("test2.html", ergebnise=rows, tittel=header, spieler=players)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask
from flask import render_template
app = Flask("yazzi")

@app.route("/")
def start():
    return render_template("start.html")

@app.route('/yazzi')
def yazzi():
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True, port=5000)
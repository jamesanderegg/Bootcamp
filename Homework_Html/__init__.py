from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/cloudiness/')
def cloudiness():
    return render_template("cloudiness.html")


@app.route('/comp/')
def comparision():
    return render_template("comp.html")


@app.route('/data/')
def data():
    return render_template("data.html")


@app.route('/humidity/')
def humidity():
    return render_template("humidity.html")


@app.route('/max/')
def max():
    return render_template("max.html")

@app.route('/wind_speed/')
def wind_speed():
    return render_template("wind_speed.html")



if __name__ == "__main__":
    app.run()
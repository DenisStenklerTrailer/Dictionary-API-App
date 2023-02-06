import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/api/v1/<word>")
def translator(word):
    definition = word.upper()
    dictionary = {"word": word, "definition": definition}

    return dictionary

if __name__ == "__main__":
    app.run(debug=True)


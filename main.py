import flask
import pandas as pd

app = flask.Flask(__name__)
df = pd.read_csv("dictionary/dictionary.csv")

@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/api/v1/<word>")
def translator(word):
    definition = df.loc[df["word"] == word]['definition'].squeeze()

    dictionary = {"word": word, "definition": definition}

    return dictionary

if __name__ == "__main__":
    app.run(debug=True)


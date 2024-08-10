from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from ice_breaker import ice_break_with

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    information = request.form["name"]

    person,organisation,transaction = ice_break_with(information=information)
    #print(jsondata)
    #import pdb;pdb.set_trace()
    return jsonify(
        {
            "person":person[1],
            "org":organisation[1],
            "transaction":transaction[1]
        }
    )


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
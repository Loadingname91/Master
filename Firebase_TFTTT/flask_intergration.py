from flask import Flask
from flask import json
from flask import request, jsonify
from initial import firebase
from firebase_integration import push_data, get_data
from flask import render_template
import os

template_dir = os.path.join(os.path.dirname(__file__), "templates")

app = Flask(__name__)


@app.route('/')
def api_root():
    return "welcome guys"


"""

Function getting post req from IFTTT trigger sends data to the firebase db 


"""


@app.route('/ifttt', methods=['POST'])
def ifthisthenthat():
    # issue with request object not
    if request.headers["Content-Type"] == "application/json":
        info_data_list = request.get_data().decode("utf-8").split(",")
        data_returned = push_data(firebase, info_data_list)
        if data_returned is "success":
            print(data_returned)
        else:
            print("fail")
    return jsonify("song added to playlist")


"""

Function getting data from the firebase database

"""


@app.route("/data_present", methods=["GET"])
def display_added():
    all_songs = get_data(firebase)
    return render_template("base.html", all_songs=all_songs.each())


if __name__ == "__main__":
    app.run(debug=True)

from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route('/')
def api_root():
    return "welcome to firebase intergration"
data = {
        "name":"Pradeep",
        "Email":"pradeppuj@gamil.com",
        "phone":9980592210
    }


@app.route('/iftt', methods=['POST'])
def ifthisthenthat():
    if request.headers["Content-Type"] == "application/json":
        info1 = json.dumps(request.json)
        info = json.loads(info1)
        print(info)
    print(request.get_data())
    return info1


if __name__ == "__main__":
    app.run(debug=True)

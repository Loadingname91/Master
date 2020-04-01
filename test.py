from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route('/')
def api_root():
    return "welcome guys"


@app.route('/github', methods=['POST'])
def github():
    if request.headers["Content-Type"] == "application/json":
        info1 = json.dumps(request.json)
        info = json.loads(info1)
        print(info["label"])
        return info1


if __name__ == "__main__":
    app.run(debug=True)

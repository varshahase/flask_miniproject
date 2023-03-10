import json
from flask import Flask, request

app = Flask(__name__)


class MyDB:
    """
    class that is runtime Database.
    NOTE -
        This DB is going to persist data as long as application is in running
        state.
    """

    foo = []


@app.get("/data")
def get_data():
    """
    HTTP GET request from postman/ browser
    Returns:
    """

    return f"<h1>data available - {MyDB.foo}</h1>"


@app.post("/data")
def post_data():
    """
    HTTP POST request with JSON payload
    Returns:
    """

    body = request.data   # byte-string
    data_ = json.loads(body)
    for value_ in data_.values():
        MyDB.foo.append(value_)

    return f"<h1>latest data - {MyDB.foo}</h1>"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)


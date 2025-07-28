from flask import Flask

app = Flask(__name__)


def rotate_antenna(direction):
    pass


@app.get("/rotate/<direction>")
def rotate(direction):
    rotate_antenna(direction)
    return f"rotating {direction}"


@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run()

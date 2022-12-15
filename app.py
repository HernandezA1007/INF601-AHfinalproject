# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Mini Project 3

# Proper import of packages used.
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Antonios Watchlist Application!'


if __name__ == '__main__':
    app.run()  # debug=True in ()



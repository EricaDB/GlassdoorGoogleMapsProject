from flask import Flask, request
from flask import render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route("/css/<path:path>")
def css(path):
    return send_from_directory('css', path)

@app.route("/js/<path:path>")
def js(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
	app.run(port = 8000)

from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(port = 8000)

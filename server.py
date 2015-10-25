from flask import Flask, request, jsonify
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

def getStockData(title):
	response = request.get('http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?symbol=AAPL&callback=myFunction').content
	return response

@app.route('/stockinfo', methods=['GET'])
def handleStockReq():
	title = request.args.get('title')
	# print getStockData(title)
	return jsonify({'stockdata': title})

if __name__ == '__main__':
	app.run(port = 8000)

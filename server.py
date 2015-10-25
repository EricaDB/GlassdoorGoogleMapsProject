from flask import Flask, request


app = Flask(__name__, static_url_path='')
app.debug = True #reload self on code changes


@app.route('/')
def hello():
	return app.send_static_file('index.html')


if __name__ == '__main__':
	app.run(host = '0.0.0.0')

#run on local host port 3008
from flask import Flask

app = Flask(__name__)
app.debug = True #reload self on code changes

@app.route('/')
def hello():
	return app.send_static_file('index.html')

if __name__ == '__main__':
	app.run()

run on local host port 3008
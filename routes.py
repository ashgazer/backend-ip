from flask import Flask, render_template, request, Markup


app = Flask(__name__)



@app.route("/")
def index():
	
	return ("<h1> boom </h1>")


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

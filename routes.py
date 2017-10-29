from flask import Flask, render_template, request, Markup

from pybay import get_s


app = Flask(__name__)



@app.route("/")
def index():
	
	return ("<h1> boom </h1>")



@app.route("/Search")
def search():
	return render_template('posting.html')


@app.route("/find",methods=['POST','GET'])
def find():
	qs =  request.form["SQUERY"]
	man = get_s()

	site_data = man.search(qs)
	site_data = site_data.replace('<a href=','<button type="submit" name="your_name" value=')


	return(site_data)


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

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


	site_data=  '<form action="/active" method="post">' + site_data + ' <input type="submit" value="Submit"> </form>'


	return(site_data)

@app.route("/active", methods=['POST'])
def active():
	tt =  request.form["your_name"]

	status = transmission()
	q = status.add_torrent(tt)

	return (q)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

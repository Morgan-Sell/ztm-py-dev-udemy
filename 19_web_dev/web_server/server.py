from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

# any time slash ("/") is selected, hi
@app.route('/')
def my_home():
	# render_template looks for a folder called "template"
	return render_template("index.html")

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about.html')
def about():
	# render_template looks for a folder called "template"
	return render_template("about.html")

@app.route('/works.html')
def works():
	return render_template("works.html")

@app.route('/contact.html')
def contact():
	return render_template("contact.html")

@app.route('/components.html')
def components():
	return render_template("components.html")




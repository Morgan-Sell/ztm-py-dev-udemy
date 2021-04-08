from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

# any time slash ("/") is selected, hi
@app.route('/<username>')
def hello_world(username=None):
	# render_template looks for a folder called "template"
	return render_template("./index.html", name=username)

@app.route('/about.html')
def about():
	# render_template looks for a folder called "template"
	return render_template("about.html")

@app.route('/blog')
def blog():
	return "These are my thoughts on blogs."


@app.route('/blog/2020/dogs')
def blog2():
	return "this is my dog"
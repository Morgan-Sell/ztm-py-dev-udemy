from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

# any time slash ("/") is selected, hi
@app.route('/')
def hello_world():
	# render_template looks for a folder called "template"
	return render_template("./index.html")

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
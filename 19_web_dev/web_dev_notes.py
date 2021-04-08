# WEB DEVELOPMENT

"""

NOTES:
-----

- HTML is the only file read by the web browser.
- href = location of the file


- python3 -m venv venv <-- creates a virtual environment

	** The second argument in the command is the location to create the virtual environment.
	   In general, I'll create it in my project and name it "venv". 
	   "venv" creates a virtual Python installation in the new "venv" folder.


To open a virtual environemnt, assuming it's called "venv", write:
	1) . venv/bin/activate
	2) source venv/bin/activate

Do not call Python file "flask.py". It will interfere with the package.

To run Flask, I must run the following:
	1) export FLASK_APP=server_file.py
	2) flask run

Must store style.css in a "static folder"

The power of Flask is that I can build a websiste dynamically.

{{ Python Expression }} - double curly brackets - instructs Flask that inside is a Python expression.

Underneath the hood of Flask is Jinja, a templating language.


Flask has variable rules that allow functions to receive <variable_name> as a keyword argument.
""
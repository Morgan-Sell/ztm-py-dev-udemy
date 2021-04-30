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
	1) export FLASK_APP=server_file.py  <-- "server_file.py" is a generic placeholder. 
	2) flask run

Must store style.css in a "static folder"

The power of Flask is that I can build a websiste dynamically.

{{ Python Expression }} - double curly brackets - instructs Flask that inside is a Python expression.

Underneath the hood of Flask is Jinja, a templating language.


Flask has variable rules that allow functions to receive <variable_name> as a keyword argument.


UUID = unique identifier

MIME = Multipruprose Internet Mail Extensions. Used by browsers to determine how to process a url. 
	** Browsers do NOT use the file extension.
	** Flasks sends the MIME type to the browser.


@app.route("/<url_param_name>")  <-- Dynamically accepts 

Must write informativon received to a file that is savined on disk. 
	** Otherwise, once the server terminates, the information is lost b/c it is stored on memory.


Two main types of DMBS:
	** Relational Databases, e.g. PostgreSQL, MySQL
		** SQL allows the the database to communicate with the Node Server.
	** Nonrelational Database, e.g. MongoDB, Cassandra
		** No schema required.
		** MongdDB is document-oriented. It stores data as documents. Each observation is its own document.

pip freeze <-- captures the package installed in the current environment.
	** pip freez > requirements.txt <-- Creates text file with all the package dependencies.



""


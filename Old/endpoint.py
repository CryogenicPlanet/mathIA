from flask import Flask,send_file

# ... other code ....
app = Flask("endpoint")
@app.route('/foo')
def file_downloads():
	try:
		return send_file('foo.csv')
	except Exception as e:
		return str(e)

from flask import Flask, render_template	##imports flask and grabs template dir
app =  Flask(__name__) ##tells flask to run the file

@app.route('/') 	##@ symbol = 'decorator' 
					##that attaches the following function to the '/'
					##so when we run localhost:5000/ 
					##the following function will run
def hello_world():
	return render_template('index.html', name="Patrick")

@app.route('/success')
def success():
	return render_template('success.html')

app.run(debug=True)	##runs in debug mode to display errors
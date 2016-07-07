from flask import Flask #imports flask
app =  Flask(__name__) #tells flask to run the file

@app.route('/') 	#@ symbol = 'decorator' 
					#that attaches the following function to the '/'
					#so when we run localhost:5000/ 
					#the following function will run
def hello_world():
	return "Hello, World!"

app.run(debug=True)	#runs in debug mode to display errors
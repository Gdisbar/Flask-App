from flask import Flask,redirect,url_for

app = Flask(__name__) # WSGI(web server gateway interface)application

@app.route('/') #@app.route(rule,options)
def fun1():
	return "Hello World ; Use url:port/ to access it"

# using dynamic url

@app.route('/Yes/<int:val>') # page url : 'Yes' so the function name : 'Yes'
def Yes(val):          
	return f"<html><body><h1>Value is {val} & the answer is Yes</h1></body></html>"


@app.route('/No/<int:val>') # page url : 'No' so the function name : 'No'
def No(val):    
	return f"<html><body><h1>Value is {val} & the answer is No</h1></body></html>"

@app.route('/results/<int:n>') #page url : 'results' so the function name : 'results'
def results(n):
	if n > 50:
		outcome="Yes" # this has to be same as the page url we want to navigate : Yes
	else:
		outcome="No" # this has to be same as the page url we want to navigate : No
	
	# url_for(url_parameter,mapping passing argument : url = current)
	return redirect(url_for(outcome,val=n))


if __name__ == '__main__':
	app.run(debug=True)
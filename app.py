from flask import Flask
import random


app = Flask(__name__) # WSGI(web server gateway interface)application

@app.route('/') #@app.route(rule,options)
def fun1():
	return "Hello World ; Use url:port/ to access it"

# using dynamic url

@app.route('/Heads/<int:coins>') 
def heads(coins):          # it's better idea to use different function name 
	def outcomes():
		x = random.uniform(0,1)
		if x > 0.5:
			return True
		else:
			return False
	results = []
	for i in range(coins):
		results.append(outcomes())
	prob = sum(results)/coins # sum counts all true values
	return f"Probability of getting Heads in {coins} coin toss is {prob}"


@app.route('/Tails/<int:coins>') 
def tails(coins):          # it's better idea to use different function name 
	def outcomes():
		x = random.uniform(0,1)
		if x > 0.5:
			return True
		else:
			return False
	results = []
	for i in range(coins):
		results.append(outcomes())
	prob = (coins - sum(results))/coins # sum counts all true values
	return f"Probability of getting Tails in {coins} coin toss is {prob}"


if __name__ == '__main__':
	app.run(debug=True)
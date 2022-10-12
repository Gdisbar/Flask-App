from flask import Flask,redirect,url_for,render_template,request
##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''

app = Flask(__name__) # WSGI(web server gateway interface)application

@app.route('/') #@app.route(rule,options)
def fun1():
	#folder name templates not template
	return render_template('index.html') 

# using dynamic url

@app.route('/status/<float:val>') 
def status(val): 
	verdict=""
	if val>50:
		verdict='PASS'
	else:
		verdict='FAIL'      
	# we'll use this 'maps' in result.html   
	# return render_template('result.html',maps=verdict) 
	# return render_template('result_1.html',maps=val) 
	exp={'val':val,'verdict':verdict}
	return render_template('result_2.html',maps=exp)


@app.route('/submit',methods=['POST','GET'])
def submit():
	avg_score=0
	if request.method=='POST':
		science=float(request.form['science']) # id from index.html
		technology=float(request.form['technology'])
		engineering=float(request.form['engineering'])
		maths=float(request.form['maths'])
		avg_score=(science+technology+engineering+maths)/4

	url = 'status'
	# url_for(url,mapping passing argument : url_param = current_val)
	return redirect(url_for(url,val=avg_score))

if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def InitialPage():
	return render_template('home.html')
	
@app.route('/<user_name>')
def auth(user_name):
	return render_template('user.html', user_name=user_name)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
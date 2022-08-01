from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'super-secret-key'


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina", "friends"]


@app.route('/',methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		username_form = request.form['username']
		password_form = request.form['password']
		if username_form == username and password_form == password:
			return redirect(url_for('home'))
		else:
			return 'Invalid password'
	else:
		return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html',facebook_friends=facebook_friends)
  

@app.route('/friend_exists/<string:name>',methods=['GET', 'POST'])
def friend(name):
	exist_friend = name in facebook_friends
	return render_template('friend_exists.html', name = name, exist_friend= exist_friend)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
from app import app, db
from flask import render_template, url_for, request, redirect
from models import user_datastore


def validation_data(args):
	for i in args:
		if len(i) == 0:
			return False
	return True

@app.route('/', methods=['GET'])
def index():
    return render_template('hello_page.html')

@app.route('/auto', methods=['GET', 'POST'])
def auto():
	if request.method == "POST":
		login = request.form['name']
		password = request.form['password']
		name = request.form['name']
		surname = request.form['surname']
		if validation_data([login, password, name, surname]):
			user_datastore.create_user(login=login, password=password,
									   name=name, surname=surname)
	else:
		login = request.args.get('name', 1)
		password = request.args.get('password', 1)
		if login != 1 and password != 1:
			pass
			
	return 'autorithation'
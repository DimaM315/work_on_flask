from app import app
from flask import render_template, url_for, request, redirect

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
			pass
	else:
		login = request.args.get('name', 1)
		password = request.args.get('password', 1)
		if login != 1 and password != 1:
			pass
			
	return 'autorithation'

@app.route('/bs/<id>', methods=['GET', 'POST'])
def user_page(id):
	if id == '1':
		return render_template('user_page.html', auto=True, check_yourPage=True,
		 contacts=[], articles=[{'id':'1','title':'Emplementation'}], login='vovcha315',
		 FI='Vladimir Eginga', )
	else:
		return render_template('404.html')

@app.route('/myWork')
def my_work():
	auto = True
	login = 'vovcha315'
	text = 'hello world'
	FI = 'Vladimir Eginga'
	title = 'My first post'
	return render_template('my_work_page.html', auto=auto,
	 login=login, text=text, FI=FI, title=title)

@app.route('/post-page/<id>', methods=['GET'])
def post_page(id):
	if id == '1':
		auto = True
		login = 'vovcha315'
		text = 'hello world, some text some text'
		post_title = 'My first post'
		author_id = 1
		author = login
		return render_template('postPage.html', auto=auto,
	 login=login, text=text, author=author, author_id=author_id, post_title=post_title)

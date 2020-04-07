from app import app, db
from flask import render_template, url_for, request, redirect, session
from models import User, validation_data, Post, is_auth



@app.route('/', methods=['GET'])
def index():
	if is_auth():
		u = User.query.filter(User.login==session['login']).first()
		return redirect(url_for('user_page', id=u.id))
	return render_template('hello_page.html')

@app.route('/auto', methods=['GET', 'POST'])
def auto():
	if request.method == "GET":
		login = request.args.get('login', '')
		password = request.args.get('password', '')
		
		if validation_data([login, password]):
			u = User.query.filter(User.login==login).first()
			if u != None and u.password == password:
				session['login'] = login
				session['password'] = password
	elif request.method == 'POST':
		login = request.form['login']
		password = request.form['password']
		name = request.form['name']
		surname = request.form['surname']
		
		if validation_data([login, password, name, surname]):	
			u = User(name=name, password=password, login=login, surname=surname)
			db.session.add(u)
			db.session.commit()
				
	return redirect(url_for('index'))


@app.route('/bs/<id>', methods=['GET', 'POST'])
def user_page(id):
	u = User.query.filter(User.id==id).first()
	if u == None:
		return render_template('404.html')
	else:
		auto = is_auth()
		#warngin!!! take another password
		check_yourPage = u.password == session['password']
		
		articles = Post.query.filter(Post.author==u.login).all()
	
	return render_template('user_page.html', auto=auto, check_yourPage=check_yourPage,
		contacts=[], articles=[{'id':a.id,'title':a.title} for a in articles], login=u.login,
		 FI=u.name+' '+u.surname)
	

@app.route('/myWork', methods=['GET'])
def my_work(message=''):
	u = User.query.filter(User.login==session['login']).first()
	if u != None and u.password == session['password']:		
		text = 'hello world'
		title = 'My first post'
		return render_template('my_work_page.html', login=u.login,
				 text=text, FI=u.name+' '+u.surname, title=title)

	return redirect(url_for('index'))

@app.route('/create_post', methods=['GET'])
def post_create():
	title = request.args.get('title', '')
	text = request.args.get('text', '')

	if len(text) < 100:
		return redirect(url_for('my_work', message='short post-body'))

	if len(title) != 0 and is_auth():
		p = Post(title=title, text=text, author=session['login'])
		db.session.add(p)
		db.session.commit()
	return redirect(url_for('index'))

@app.route('/post-page/<id>', methods=['GET'])
def post_page(id):
	if int(id) > 0:
		p = Post.query.filter(Post.id==id).first()
		if p == None:
			return render_template('404.html')
		text = p.text
		post_title = p.title
		author_id = User.query.filter(User.login==p.author).first().id
		author = p.author
		
		return render_template('postPage.html', auto=is_auth(),
	 login=session['login'], text=text, author=author, author_id=author_id, post_title=post_title)
	else:
		return 'invalid id-post'

@app.route('/logout')
def logout():
	session.pop('login', None)
	session.pop('password', None)
	return redirect(url_for('index'))
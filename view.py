from app import app, db
from flask import render_template, url_for, request, redirect, session
from models import User, validation_data, Post, is_auth
import re



@app.route('/', methods=['GET'])
def index():
	if is_auth():
		u = User.query.filter(User.login==session['login']).first()
		return redirect(url_for('user_page', nickname_or_id=u.id))
	return render_template('hello_page.html')

@app.route('/auto', methods=['GET', 'POST'])
def auto():
	if request.method == "GET":
		#autho
		login = request.args.get('login', '').strip()
		password = request.args.get('password', '').strip()
		
		if validation_data([login, password]):
			u = User.query.filter(User.login==login).first()
			if u != None and u.password == password:
				session['login'] = login
				session['password'] = password
	elif request.method == 'POST':
		#reg
		login = request.form['login'].strip()
		password = request.form['password'].strip()
		name = request.form['name'].strip()
		surname = request.form['surname'].strip()
		
		if validation_data([login, password, name, surname]):	
			u = User(name=name, password=password, login=login, surname=surname)
			db.session.add(u)
			db.session.commit()
				
	return redirect(url_for('index'))

@app.route('/bs/<nickname_or_id>', methods=['GET', 'POST'])
def user_page(nickname_or_id):
	for i in range(len(nickname_or_id)):
		if re.fullmatch('\D+', nickname_or_id[i]):
			u = User.query.filter(User.login==nickname_or_id).first()
			break
	else:
		u = User.query.filter(User.id==nickname_or_id).first() or None
		if u == None:
			return render_template('404.html')
	
	
	auto = is_auth()
	check_friend = False
	#warngin!!! take another password
	check_yourPage = u.password == session['password']
	
	if u.contacts != '':
		contacts = [{'nickname' : c, 'FI' : 
					User.query.filter(User.login==c).first().name+' '+
					User.query.filter(User.login==c).first().surname}
					for c in u.contacts.split('/#/')]
	else:
		contacts = []

	if auto and not check_yourPage:
		my = User.query.filter(User.login==session['login']).first()
		check_friend = u.login in my.contacts.split('/#/')
	
	articles = Post.query.filter(Post.author==u.login).all()
	
	return render_template('user_page.html',
			auto=auto, 
			check_yourPage=check_yourPage,
			check_friend = check_friend,
			contacts=contacts, 
			articles=[{'id':a.id,'title':a.title} for a in articles], 
			login=u.login, FI=u.name+' '+u.surname)

@app.route('/add_contact', methods=['GET'])
def manipulate_contacts(login='', action=''):
	login = request.args.get('login', '')
	action = request.args.get('action', '')
	if is_auth():
		u = User.query.filter(User.login==session['login']).first()
		if action == 'add':
			if u.contacts == '':
				u.contacts = str(login)
			else:
				u.contacts += '/#/'+str(login)

		elif action == 'delete':
			if u.contacts == '':
				pass
			else:
				contacts = u.contacts.split('/#/')
				contacts.remove(login)
				u.contacts = '/#/'.join(contacts)
			
		db.session.add(u)
		db.session.commit()
	return redirect(url_for('index'))

@app.route('/myWork', methods=['GET'])
def my_work(message=''):
	u = User.query.filter(User.login==session['login']).first()
	if u.password == session['password']:		
		return render_template('my_work_page.html', 
				login=u.login,
				text='', 
				FI=u.name+' '+u.surname,
				title='')
	return redirect(url_for('index'))

@app.route('/create_post', methods=['GET'])
def post_create():
	title = request.args.get('title', '').strip()
	text = request.args.get('text', '').strip() #убираем пробелы с боков

	if len(text) < 100 or len(title) < 5:
		return redirect(url_for('my_work', message='short post-data'))

	if is_auth():
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
		author_id = User.query.filter(User.login==p.author).first().id
		
		return render_template('postPage.html', auto=is_auth(),
						login=session['login'], text=p.text, author=p.author,
						author_id=author_id, post_title=p.title)
	else:
		return 'invalid id-post'

@app.route('/logout')
def logout():
	session.pop('login', None)
	session.pop('password', None)
	return redirect(url_for('index'))
from app import app
import controllers


@app.route('/', methods=['GET'])
def index():
	return controllers.PageController().call(page='index')


@app.route('/enter/<act>', methods=['GET', 'POST'])
def enter(act):
	return controllers.UserController().call(act=act)


@app.route('/user/<nickname_or_id>', methods=['GET', 'POST'])
def user_page(nickname_or_id):
	return controllers.PageController().call(page='user', nickname_or_id=nickname_or_id)


@app.route('/add_contact', methods=['GET'])
def manipulate_contacts():
	return controllers.UserController().call(act='add_contact')


@app.route('/myWork', methods=['GET'])
def my_work():
	return controllers.PageController().call(page='myWork')


@app.route('/create_post', methods=['POST'])
def post_create():
	return controllers.PostController.create_post()


@app.route('/delete_post/<post_id>', methods=['POST'])
def delete_post(post_id):
	return controllers.PostController.delete_post(post_id)


@app.route('/post/<id>', methods=['GET'])
def post_page(id):
	return controllers.PageController().call(page="post", post_id=id)


@app.route('/logout')
def logout():
	return controllers.UserController.logout()

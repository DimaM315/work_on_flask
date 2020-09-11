from controllers.BaseController import *
from controllers.UserController import UserController
from controllers.PostController import PostController


class PageController(BaseController):
    def _call(self, *args, **kwargs):
        page = kwargs.get('page', False)
        if page == 'index':
            return self.index_page()
        elif page == 'myWork':
            return self.myWork_page()
        elif page == 'post':
            return self.post_page(kwargs['post_id'])
        elif page == 'user':
            return self.user_page(kwargs['nickname_or_id'])


    def index_page(self):
        if is_auth():
            u = User.select().where(User.login == session.get('login', '')).first()
            return redirect(url_for('user_page', nickname_or_id=u.id))
        return render_template('hello_page.html')

    def myWork_page(self):
        if is_auth():
            u = User.select().where(User.login == session.get('login', '')).first()
            myWork_data = {
                'login': u.login,
                'text': '',
                'FI': '{} {}'.format(u.name, u.surname),
                'title': ''
            }
            return render_template('my_work_page.html', **myWork_data)
        return redirect(url_for('index'))

    def post_page(self, id):
            return render_template('postPage.html', **PostController.get_post_data(id))

    def user_page(self, nickname_or_id):
        assert len(nickname_or_id) > 0
        u = UserController.get_user_by_nick_or_id(nickname_or_id)
        if u == None:
            return render_template('404.html')

        user_page_data = UserController.get_user_page_data(u)
        return render_template('user_page.html', **user_page_data)

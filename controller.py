from flask import request, render_template, make_response, url_for
from models import *


class BaseController:
    def __init__(self):
        self.request = request

    def call(self, *args, **kwargs):
        print('in call')
        try:
            return self._call(*args, **kwargs)
        except Exception as ex:
            return make_response(str(ex), 500)

    def __call(self, *args, **kwargs):
        raise NotImplementedError('_call')


class UserController(BaseController):
    def _call(self, *args, nickname_or_id=False, **kwargs):
        if nickname_or_id:
            return self.get_user_page(nickname_or_id)

    def get_user_page(self, nick_or_id):
        assert nick_or_id == type('str') and len(nick_or_id) >= 1
        u = self.get_user_by_nick_or_id(nick_or_id)
        if u == None:
            render_template('404.html')

        page_data = {'auto': is_auth(),
                     'check_yourPage': u.password == session['password'],
                     'check_friend': False,
                     'contacts': self.get_user_contacts(u),
                     'login': '{} {}'.format(u.name, u.surname),
                     'articles': []
        }
        if page_data['auto'] and not page_data['check_yourPage']:
            # when the user went to another user`s page
            my = User.query.filter(User.login == session['login']).first()
            page_data['check_friend'] = u.login in my.contacts.split('/#/')

        articles_data = Post.query.filter(Post.author == u.login).all()
        page_data['articles'] = [{'id': a.id, 'title': a.title} for a in articles_data]

        return render_template('user_page.html', **page_data)

    def get_user_contacts(self, user):
        contacts = []
        # parse value of contacts field
        if user.contacts != '':
            # nick - nickname which having contact of our user
            for nick in user.contacts.split('/#/'):
                c = User.query.filter(User.login == c).first()
                contacts.append({
                    'nickname': nick,
                    'FI': '{} {}'.format(c.name, c.surname)})

        return contacts

    def get_user_by_nick_or_id(self, nick_or_id):
        # define the type of nickname_or_id
        str_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if nick_or_id[0] in str_nums:
            # is id
            u = User.query.filter(User.id == nick_or_id).first() or None
        else:
            # is nickname
            u = User.query.filter(User.login == nick_or_id).first() or None
        return u

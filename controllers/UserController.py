from controllers.BaseController import *


class UserController(BaseController):
    def _call(self, *args, **kwargs):
        act = kwargs.get('act')

        if act == 'reg':
            return self.reg()
        elif act == 'auto':
            return self.auto()
        elif act == 'add_contact':
            return self.do_contact()

    @staticmethod
    def get_user_page_data(user):
        page_data = {'auto': is_auth(),
                     'check_yourPage': session.get('login', '') == user.login,
                     'in_friends': False,
                     'contacts': UserController.get_user_contacts(user),
                     'login': session.get('login', ''),
                     'own': user.login,
                     'FI': '{} {} ({})'.format(user.name, user.surname, user.login),
                     'articles': []
        }
        if page_data['auto'] and not page_data['check_yourPage']:
            # when the user went to another user`s page
            client = User.select().where(User.login == session['login']).first()
            page_data['in_friends'] = user.login in client.contacts.split('/#/')

        articles_data = list(Post.select().where(Post.author == user.login))
        page_data['articles'] = [{'id': a.id, 'title': a.title} for a in articles_data]

        return page_data

    @staticmethod
    def logout():
        session.pop('login', None)
        session.pop('password', None)
        return redirect(url_for('index'))

    @staticmethod
    def get_user_contacts(user):
        contacts = []
        # parse value of contacts field
        if user.contacts != '':
            # nick - nickname which having contact of our user
            for nick in user.contacts.split('/#/'):
                c = User.select().where(User.login==nick).first()
                contacts.append({
                    'nickname': nick,
                    'FI': '{} {}'.format(c.name, c.surname)})

        return contacts

    @staticmethod
    def get_user_by_nick_or_id(nick_or_id):
        # define the type of nickname_or_id
        digital_char = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        if nick_or_id[0] in digital_char:
            # is id
            u = User.select().where(User.id == nick_or_id).first() or None
        else:
            # is nickname
            u = User.select().where(User.login == nick_or_id).first() or None
        return u

    def auto(self):
        login = self.request.args.get('login', '').strip()
        password = self.request.args.get('password', '').strip()

        if validation_data([login, password]):
            u = User.select().where(User.login == login).first()
            if u != None and u.password == password:
                session['login'] = login
                session['password'] = password
        return redirect(url_for('index'))

    def reg(self):
        assert self.request.method == "POST"

        login = self.request.form['login'].strip()
        password = self.request.form['password'].strip()
        name = self.request.form['name'].strip()
        surname = self.request.form['surname'].strip()

        if validation_data([login, password, name, surname]):
            u = User(name=name, password=password, login=login, surname=surname, contacts='')
            u.save()
        return redirect(url_for('index'))

    def do_contact(self):
        contact = self.request.args.get('who', False)
        action = self.request.args.get('action', False)
        if is_auth() and contact and action:
            u = User.select().where(User.login == session['login']).first()
            if action == 'add':
                if u.contacts == '':
                    u.contacts = contact
                else:
                    u.contacts += '/#/' + contact
            elif action == 'delete':
                if u.contacts != '':
                    contacts = u.contacts.split('/#/')
                    contacts.remove(contact)
                    u.contacts = '/#/'.join(contacts)
            u.save()
        return redirect(url_for('index'))
		



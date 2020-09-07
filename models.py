from app import db
# from flask_security import SQLAlchemyUserDatastore, Security, current_user
# from flask_security import UserMixin, RoleMixin
import re
from flask import session


def validation_data(args):
    for i in args:
        if len(i) < 3:
            return False
    return True


def slugify(title):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', title)


def is_auth():
    login = session.get('login', False)
    password = session.get('password', False)
    if login == False or password == False:
        return False
    u = User.query.filter(User.login == login).first()
    return u.password == password


role_users = db.Table('role_users',
                      db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                      db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
                      )


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(140), unique=True)
    password = db.Column(db.String(255))

    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))

    contacts = db.Column(db.String(255))

    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=role_users,
                            backref=db.backref('user', lazy='dynamic'))

    def __init__(self):
        super(Post, self).__init__(*args, **kwags)
        contacts = ''


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(140), unique=True)
    discription = db.Column(db.String(255))


post_tag = db.Table('post_tags',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                    )


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(140), unique=True)
    text = db.Column(db.Text)
    author = db.Column(db.String(140))
    likes = db.Column(db.Integer())
    tag = db.relationship('Tag', secondary=post_tag,
                          backref=db.backref('posts', lazy='dynamic'))
    slug = db.Column(db.String(140), unique=True)

    def __init__(self, *args, **kwags):
        super(Post, self).__init__(*args, **kwags)
        self.slug = slugify(self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)

    def __init__(self, *args, **kwags):
        super(Tag, self).__init__(*args, **kwags)
        self.slug = slugify(self.name)

### Flask - security

# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

from app import db
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask_security import UserMixin, RoleMixin



role_users = db.Table('role_users',
			db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
			db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	login = db.Column(db.String(140), unique=True)
	password = db.Column(db.String(255))

	name = db.Column(db.String(255))
	surname = db.Column(db.String(255))

	active = db.Column(db.Boolean())
	roles = db.relationship('Role', secondary=role_users,
						backref=db.backref('user', lazy='dynamic'))
	
	
class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(140), unique=True)
	discription = db.Column(db.String(255))




### Flask - security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
#security = Security(app, user_datastore)
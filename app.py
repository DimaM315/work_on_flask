from flask import Flask, request, redirect, url_for
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager







app = Flask(__name__)
#Класс фласк принимает имя файла(__name__), что бы знать текущее место на диске
#и самостоятельно находить шаблоны и пр.
app.config.from_object(Configuration)

db = SQLAlchemy(app)



migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
'''
##### Admin #####
from models import *

class AminMinix:
#переопределяем методы
	def is_accessible(self):
		return current_user.has_role('admin')
	
	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('security.login', next=request.url))


class AnminView(AminMinix, ModelView):
#чтобы переопделение сработало, ставим "свежие" методы в начало
	pass

class HomeAdminView(AminMinix,AdminIndexView):
#чтобы переопделение сработало, ставим "свежие" методы в начало
	pass

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(AnminView(Post, db.session))
admin.add_view(AnminView(Tag, db.session))




### Flask - security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
'''
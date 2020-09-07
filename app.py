from flask import Flask, request, redirect, url_for
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager






app = Flask(__name__)
#Класс фласк принимает имя файла(__name__), что бы знать текущее место на диске
#и самостоятельно находить шаблоны и пр.
app.config.from_object(Configuration)

db = SQLAlchemy(app)


#Mirgation
mirgate = Migrate(app, db)
manager = Manager(app)
#regisrtated command 'db'
manager.add_command('db', MigrateCommand)
from peewee import (Model, IntegerField, DoubleField, CharField, BooleanField,
                    PrimaryKeyField, TextField, 
                    DateTimeField, datetime as peewee_datetime,)
from flask import session
from app import db_peewee
import re


class _Model(Model):
	class Meta:
		database = db_peewee


class Articles(_Model):
	class Meta:
		db_table = 'articles'


class User(_Model):
    class Meta:
        db_table = 'users'

    id = PrimaryKeyField(null=False)
    login = CharField(max_length=140, index=True)
    password = CharField(max_length=25)

    name = CharField(max_length=35, null=False)
    surname = CharField(max_length=35, null=False)

    contacts = TextField(null=True)

    active = BooleanField(default=True)
    #roles = db.relationship('Role', secondary=role_users,
                           # backref=db.backref('user', lazy='dynamic'))

class Post(_Model):
    class Meta:
        db_table = 'posts'

    id = PrimaryKeyField(null=False)
    title = CharField(max_length=35, null=False)
    text = TextField(null=False)
    author = CharField(max_length=35, null=False)
    likes = TextField(null=True)
    #tag = db.relationship('Tag', secondary=post_tag,
                         # backref=db.backref('posts', lazy='dynamic'))
    slug = CharField(max_length=35, null=False)
'''
Models for user, blog, comment.
'''

__author__='Kevinlin'

import time, uuid

from orm import Model, SrtingField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = SrtingField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = SrtingField(ddl='varchar(50)')
    passwd = SrtingField(ddl='varchar(50)')
    admin = BooleanField()
    name = SrtingField(ddl='varchar(50)')
    image = SrtingField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__='blogs'

    id = SrtingField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = SrtingField(ddl='varchar(50)')
    user_name = SrtingField(ddl='varchar(50)')
    user_image = SrtingField(ddl='varchar(500)')
    name = SrtingField(ddl='varchar(50)')
    summary = SrtingField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__='comments'

    id = SrtingField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = SrtingField(ddl='varchar(50)')
    user_id = SrtingField(ddl='varchar(50)')
    user_name = SrtingField(ddl='varchar(50)')
    user_image = SrtingField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

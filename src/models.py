import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True) 
    username = Column(String(15), nullable=False, unique=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False, unique=True)

class Follower(Base):
    __tablename__ = 'follower'
#Convertimos user_from_id y user_to_id en llaves primarias(compuestas) para evitar que un usuario siga a otro más de una vez.
#A la vez son llaves foráneas para poder relacionarlas con la tabla "user".
    user_from_id = Column(Integer, ForeignKey('User.user_id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('User.user_id'), primary_key=True)
#Esta línea asegura que user_from_id y user_to_id no sean iguales(Que un usuario no se siga asi mismo).
#CheckConstraint hay que importarlo.
    __table_args__ = (CheckConstraint('user_from_id <> user_to_id', name='check_user_ids_not_equal'),)

class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    #Define un tipo Enum con los valores 'image', 'video' y 'audio'. El parámetro name especifica el nombre del tipo enum en la base de datos.
    #Definimos Enum con uno de los siguientes valores 'image, video audio'
    #Y Le damos un nombre al conjunto de valores (name= name_type).
    type = Column(Enum('image', 'video', 'image', name='media_type'), nullable=False)
    url = Column(String, unique=True)
    post_id = Column(Integer, ForeignKey('Post.user_id'))

class Post(Base):
     __tablename__ = 'post'
     post_id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('User.user.id'))

class Comment(Base):
     __tablename__ = 'comment'
     comment_id = Column(Integer, primary_key=True)
     comment_text = Column(String(200))
     author_id = Column(Integer, ForeignKey('User.user_id'))
     post_id = Column(Integer, ForeignKey('Post.post_id'))

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

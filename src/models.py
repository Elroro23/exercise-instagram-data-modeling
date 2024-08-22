import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
#Las FK normalmente son las que se relacionan con las PK.
#Luego de definir la relación de la FK hay que especificar a la tabla que está ese id.
#Los nombres de las tablas van en minúsculas(buenas prácticas).
#Para representar una relación de muchos a muchos hay que hacer una tabla intermedia.
#Convertir esos id en PK compuestas(dos llaves primarias) y a su vez hacerlas FK y luego relacionar esos id con los id de las tablas que quieres relacionar.
#UNIQUE: el campo debe ser único.
#nullable=False: Significa que ese campo no puede estar vacío.
class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True) 
    user_name = Column(String(15), nullable=False, unique=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False, unique=True)

class Follower(Base):
    __tablename__ = 'follower'
    follower_id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.user_id'))
    user_from_id_relationship = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.user_id'))
    user_to_id_relationship = relationship(User)

class Address(Base):
     __tablename__ = 'address'
     address_id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.user_id'))
     user_id_relationship = relationship(User)
     street_name = Column(String(50), nullable=False)
     street_number = Column(Integer, nullable=False)
     post_code = Column(Integer, nullable=False)

class Post(Base):
     __tablename__ = 'post'
     post_id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.user.id'))
     user_id_relationship = relationship(User)

class Comment(Base):
     __tablename__ = 'comment'
     comment_id = Column(Integer, primary_key=True)
     comment_text = Column(String(200), nullable=False)
#No relaciono directamente el user_id(Comment) con User porque ya existe una relación indirecta entre user_id(Post) y User.
#Pero user_id(Comment) sigue siendo importante para identificar quien hizo el comentario.
     user_id = Column(Integer) 
     post_id = Column(Integer, ForeignKey('post.post_id'))
     post_id_relationship = relationship(Post)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

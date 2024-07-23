import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    created_at = Column(DateTime, nullable=False)
    favorite = relationship('Favorite', backref='user', lazy=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'), nullable=True)
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'), nullable=True)
    
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    manufacturer = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    capacity = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'), nullable=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

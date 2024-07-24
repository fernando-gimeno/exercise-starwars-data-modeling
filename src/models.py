import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    created_at = Column(DateTime, nullable=False)
    favorites = relationship('Favorite', backref='users', lazy=True)

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    
class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    
class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    manufacturer = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    capacity = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

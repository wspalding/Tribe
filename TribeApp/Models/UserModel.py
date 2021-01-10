from TribeApp import db
from flask_login import UserMixin

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash, check_password_hash


import uuid

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(UUID(as_uuid=True), 
                        primary_key=True, 
                        default=uuid.uuid4, 
                        unique=True, 
                        nullable=False)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tribe_id = Column(UUID(as_uuid=True), ForeignKey('Tribe.id'),
                        nullable=True,
                        default=None)
    tribe = relationship('Tribe')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)
        

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
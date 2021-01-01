from TribeApp import db

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import uuid

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(UUID(as_uuid=True), 
                        primary_key=True, 
                        default=uuid.uuid4, 
                        unique=True, 
                        nullable=False)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tribe_id = Column(UUID(as_uuid=True), 
                            ForeignKey('Tribe.id'), 
                            nullable=True,
                            default=None)

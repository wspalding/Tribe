from TribeApp import db

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base 
import uuid

class Tribe(db.Model):
    __tablename__ = 'Tribe'
    id = db.Column(UUID(as_uuid=True), 
                        primary_key=True, 
                        default=uuid.uuid4, 
                        unique=True, 
                        nullable=False)
    name = db.Column(db.String(64), index=True)
    slug = db.Column(db.String(64), unique=True)
    members = relationship('User', back_populates='User')

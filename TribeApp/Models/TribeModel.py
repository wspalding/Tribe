from TribeApp import db

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.types import ARRAY
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
    members = db.relationship('User', 
                                backref='Tribe', 
                                lazy=True)
    posersonality_vector = db.Column(ARRAY(Integer, dimensions=5), 
                                        nullable=True, 
                                        default=None)

    def __init__(self, name):
        self.name = name
        self.slug = self.create_slug(name)

    def create_slug(self, name):
        return name.title().replace(' ', '')
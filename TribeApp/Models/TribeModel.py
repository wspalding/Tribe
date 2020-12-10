from TribeApp import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Tribe(db.Model):
    id = db.Column(UUID(as_uuid=True), 
                        primary_key=True, 
                        default=uuid.uuid4, 
                        unique=True, 
                        nullable=False)

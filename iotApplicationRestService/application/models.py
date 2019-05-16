from datetime import datetime
from config import db, ma

class NetworkMetadata(db.Model):
    __tablename__ = "network_metadata"
    sense_time = db.Column(db.Integer, primary_key=True)

class NetworkMetadataSchema(ma.ModelSchema):
    class Meta:
        model = NetworkMetadata
        sqla_session = db.session

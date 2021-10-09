from flask_sqlalchemy import SQLAlchemy, Pagination
from datetime import datetime
from sqlalchemy.sql import text

db = SQLAlchemy()


class Object(db.Model):
    __tablename__ = 'objects'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column('date', db.DateTime(), default=datetime.utcnow, nullable=False)
    name = db.Column('name', db.String(50), nullable=False)
    quantity = db.Column('quantity', db.Integer(), nullable=False)
    distance = db.Column('distance', db.Integer(), nullable=False)

    def __repr__(self):
        return '<Type {}>'.format(self.id)
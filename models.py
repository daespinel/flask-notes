from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    update_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    update_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
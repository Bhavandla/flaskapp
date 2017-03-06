from app import db, lm
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin


class User(UserMixin, db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  social_id = db.Column(db.String(64), nullable= False, unique=True)
  nickname = db.Column(db.String(64), nullable=False)
  email = db.Column(db.String(64), nullable=True)

@lm.user_loader
def load_user(id):
  return User.query.get(int(id))

"""class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)
      
class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(140))
  timestamp = db.Column(db.DateTime)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
  def __repr__(self):
    return '<post %r>' % (self.body) 
"""
  
  
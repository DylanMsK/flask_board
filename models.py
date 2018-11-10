from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

class Post(db.Model):
    # db table 설정
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)    # PK로 지정
    title = db.Column(db.String, nullable=False)    # null값 불가능
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref='post')
    
    # 생성자
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()
        

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String)
    content = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    created_at = db.Column(db.DateTime)
    
    def __init__(self, content, user_id):
        self.content = content
        self.created_at = datetime.datetime.now()
        self.user_id = user_id
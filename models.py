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
    
    # 생성자
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()
        
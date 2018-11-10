from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import *
import os

app = Flask(__name__)

# DB 설정
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///board'   # 초기에 DB create 할때 지정한 db이름 board
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    # posts = Post.query.all()    # SELECT * FROM posts;
    posts = Post.query.order_by(Post.id.desc()).all()   # SELECT * FROM posts ORDER BY id DESC;
    return render_template('index.html', posts=posts)

@app.route('/posts/new')
def new():
    return render_template('new.html')
    
@app.route('/posts/create', methods=['POST'])
def create():
    # title = request.args.get('title')     # get 방식에서 request받기
    # content = request.args.get('content')
    title = request.form.get('title')       # post방식에서 request받기
    content = request.form.get('content')
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return redirect('/posts/{}'.format(post.id))
    
@app.route('/posts/<int:id>')
def read(id):
    post = Post.query.get(id)   # SELECT * FROM posts WHERE id=1;
    return render_template('read.html', post=post)
    
@app.route('/posts/<int:id>/delete')
def delete(id):
    post = Post.query.get(id)   # DELETE FROM posts WHERE id=#;
    db.session.delete(post)
    db.session.commit()
    return redirect('/')
    
@app.route('/posts/<int:id>/edit')
def edit(id):
    post = Post.query.get(id)
    return render_template('edit.html', post=post)
    
@app.route('/posts/<int:id>/update', methods=['POST'])
def update(id):
    post = Post.query.get(id)
    post.title = request.form.get('title')
    post.content = request.form.get('content')
    post.created_at = request.form.get('created_at')
    db.session.commit()
    return redirect('/posts/{}'.format(id))

@app.route('/posts/<int:post_id>/comment', methods=['POST'])
def comment(post_id):
    content = request.form.get('content')
    user_id = request.form.get('user_id')
    comment = Comment(content, user_id)
    post = Post.query.get(post_id)
    post.comments.append(comment)
    db.session.add(comment)
    db.session.commit()
    return redirect('/posts/{}'.format(post_id))
    
@app.route('/comment/<int:comment_id>/delete')
def comment_delete(comment_id):
    comment = Comment.query.get(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect('/posts/{}'.format(comment.post_id))
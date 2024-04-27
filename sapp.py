from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    # Add logic to fetch and display portfolio items
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    posts = Post.query.all()
    return render_template('blog.html', posts=posts)

@app.route('/blog/post/<int:id>')
def view_post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
